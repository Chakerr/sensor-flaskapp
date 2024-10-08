#Proyecto: Sensor de Distancia con Visualización en Tiempo Real

Este proyecto mide la distancia utilizando un sensor conectado a un **Arduino**, visualiza los datos en tiempo real mediante una **página web**, y almacena las mediciones en una base de datos **SQLite**.

## Requisitos

- **Arduino** con sensor de distancia (como el HC-SR04).
- **Python 3.x** instalado en el sistema.
- **Flask** para el servidor web.
- **SQLite** para la base de datos.
- **Permisos de escritura** en la carpeta `/var/www/html` (en sistemas Linux).

##Instalación y Configuración

### 1. Clonar el Repositorio

Ejecuta los siguientes comandos para clonar el repositorio en la carpeta `/var/www/html` o en la ubicación que prefieras:

```bash
cd /var/www/html
git clone https: https://github.com/Chakerr/sensor-flaskapp.git
cd sensor-flaskapp
```

### 2. Instalar Dependencias

Asegúrate de tener **Python 3** y **pip** instalados en tu sistema. Luego, instala las dependencias necesarias:

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip sqlite3
sudo pip3 install Flask
```
### 3. Configuración del Puerto Serial

Edita el archivo `app.py` para que el puerto serial coincida con el puerto donde está conectado tu Arduino:

```python
arduino_port = "/dev/ttyUSB0"  # Cambiar al puerto correspondiente
```
### 4. Permisos

Dado que el proyecto está ubicado en la carpeta `/var/www/html`, asigna los permisos adecuados para evitar problemas de acceso:

```bash
sudo chmod -R 755 /var/www/html/sensor-flaskapp
```
##Ejecución

### 1. Ejecutar el Servidor

Navega a la carpeta del proyecto y ejecuta el servidor Flask:

```bash
cd /var/www/html/sensor-flaskapp
sudo python3 app.py
```

### 2. Visualización en Tiempo Real

Los datos del sensor se visualizarán en tiempo real en una gráfica en la página principal. Además, puedes ver las mediciones almacenadas en la base de datos a través de las siguientes rutas:

- **Página Principal**: `http://tu-ip:5000/`

## 🛠 Estructura del Proyecto

```bash
sensor-datos-web/
│
├── app.py               # Script principal que gestiona la conexión al Arduino y la web
├── templates/      
│   └── sensor.html      # Página web principal
├── mediciones.db        # Base de datos SQLite donde se almacenan las mediciones
└── README.md            # Archivo de documentación del proyecto
```
## Pruebas

Para asegurarte de que todo está funcionando correctamente, sigue estos pasos:

1. Conecta el Arduino al puerto USB.
2. Ejecuta el servidor con `python3 app.py`.
3. Abre el navegador y accede a `http://tu-ip:5000/`.
4. Verifica que los datos del sensor se muestren en la gráfica y en la tabla.

## Notas Adicionales

- **Recuerda modificar el puerto serial** en `app.py` según tu configuración.
- El proyecto está diseñado para funcionar en sistemas Linux, pero debería ser fácilmente adaptable a otros entornos.

## 📄 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).
