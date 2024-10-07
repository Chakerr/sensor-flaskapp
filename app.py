from flask import Flask, render_template, Response
import serial
import time
import json
import sqlite3

app = Flask(__name__)

# Configuración del puerto serial
arduino_port = "/dev/ttyUSB0"  # Cambia esto a tu puerto correcto
baud = 9600
ser = serial.Serial(arduino_port, baud, timeout=1)
time.sleep(2)  # Esperar que el puerto serial se inicialice

# Variable para contar el tiempo en segundos
tiempo_conectado = 0

# Conexión a la base de datos SQLite
conn = sqlite3.connect('mediciones.db', check_same_thread=False)
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS datos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tiempo INTEGER,
                    distancia INTEGER
                )''')
conn.commit()

# Limpiar la tabla y reiniciar el índice
cursor.execute("DELETE FROM datos")  # Limpia la tabla
cursor.execute("DELETE FROM sqlite_sequence WHERE name='datos'")  # Reinicia el índice
conn.commit()

@app.route('/')
def index():
    return render_template('sensor.html')  # Renderiza la página de la gráfica

def generar_datos():
    global tiempo_conectado
    while True:
        if ser.in_waiting > 0:
            linea = ser.readline().decode('utf-8').strip()
            if "Distancia" in linea:
                distancia = int(linea.split()[1])
                tiempo_conectado += 1  # Incrementar el contador de tiempo conectado

                # Guardar en la base de datos
                cursor.execute("INSERT INTO datos (tiempo, distancia) VALUES (?, ?)", (tiempo_conectado, distancia))
                conn.commit()

                # Crear un diccionario con los datos
                data = {'tiempo': tiempo_conectado, 'distancia': distancia}
                yield f"data: {json.dumps(data)}\n\n"  # Formato SSE

@app.route('/datos')
def datos():
    return Response(generar_datos(), mimetype='text/event-stream')

# Ruta para ver los datos en formato JSON
@app.route('/ver_datos')
def ver_datos():
    cursor.execute("SELECT * FROM datos")
    registros = cursor.fetchall()
    datos = [{'id': row[0], 'tiempo': row[1], 'distancia': row[2]} for row in registros]
    return json.dumps(datos)

# Ruta para ver los datos en una tabla HTML
@app.route('/ver_datos_html')
def ver_datos_html():
    cursor.execute("SELECT * FROM datos")
    registros = cursor.fetchall()
    datos = [{'id': row[0], 'tiempo': row[1], 'distancia': row[2]} for row in registros]
    return render_template('ver_datos.html', datos=datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Cambia la dirección IP a 0.0.0.0 para escuchar en todas las interfaces
