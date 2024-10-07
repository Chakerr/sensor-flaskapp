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

## Código del Arduino

Este es el código que debes cargar en tu Arduino para medir la distancia con un sensor ultrasónico.

```cpp
#define TRIG_PIN 9  // Pin digital conectado al TRIG del sensor ultrasónico
#define ECHO_PIN 10 // Pin digital conectado al ECHO del sensor ultrasónico

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);
  int distance = duration * 0.034 / 2;

  Serial.print("Distancia: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(1000);
}
