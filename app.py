from flask import Flask, render_template, Response
import serial
import time
import json
import sqlite3

app = Flask(__name__)

arduino_port = "/dev/ttyUSB0"  # Cambia esto a tu puerto correcto
baud = 9600
ser = serial.Serial(arduino_port, baud, timeout=1)
time.sleep(2)  
tiempo_conectado = 0
conn = sqlite3.connect('mediciones.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS datos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tiempo INTEGER,
                    distancia INTEGER
                )''')
conn.commit()
cursor.execute("DELETE FROM datos")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='datos'")
conn.commit()
@app.route('/')
def index():
    return render_template('sensor.html')
def generar_datos():
    global tiempo_conectado
    while True:
        if ser.in_waiting > 0:
            linea = ser.readline().decode('utf-8').strip()
            if "Distancia" in linea:
                distancia = int(linea.split()[1])
                tiempo_conectado += 1
                cursor.execute("INSERT INTO datos (tiempo, distancia) VALUES (?, ?)", (tiempo_conectado, distancia))
                conn.commit()
                data = {'tiempo': tiempo_conectado, 'distancia': distancia}
                yield f"data: {json.dumps(data)}\n\n"
@app.route('/datos')
def datos():
    return Response(generar_datos(), mimetype='text/event-stream')
@app.route('/ver_datos')
def ver_datos():
    cursor.execute("SELECT * FROM datos")
    registros = cursor.fetchall()
    datos = [{'id': row[0], 'tiempo': row[1], 'distancia': row[2]} for row in registros]
    return json.dumps(datos)
@app.route('/ver_datos_html')
def ver_datos_html():
    cursor.execute("SELECT * FROM datos")
    registros = cursor.fetchall()
    datos = [{'id': row[0], 'tiempo': row[1], 'distancia': row[2]} for row in registros]
    return render_template('ver_datos.html', datos=datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
