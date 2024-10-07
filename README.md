# Proyecto de Sensor de Distancia con Flask y Arduino

Este proyecto utiliza un sensor ultrasónico conectado a un Arduino para medir la distancia y mostrarla en una aplicación web creada con Flask.

## Requisitos

- Python 3.x
- Arduino
- Flask
- pySerial

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tuusuario/nombre-del-repositorio.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd nombre-del-repositorio
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Carga el código en tu Arduino. Abre el archivo `distance_sensor.ino` en el IDE de Arduino, selecciona tu placa y puerto, y súbelo al Arduino.

5. Ejecuta la aplicación Flask:

    ```bash
    python app/app.py
    ```

6. Abre tu navegador y navega a `http://127.0.0.1:5000` para ver la distancia medida por el sensor.

