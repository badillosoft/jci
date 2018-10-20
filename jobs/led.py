import RPi.GPIO as GPIO
import sys
import json

# Paso 1 - Recuperar los parametros del Job como un diccionario JSON
data = json.loads(sys.argv[1])
# Paso 2 - Recuperar el pin del led y el modo de encendido/apagado
pin = int(data["pin"])
mode = data["mode"]

# Paso 3 - Encendemos el led con el pin y dependiendo el modo encendemos o apagamos

# Ajustamos a BCM la numeracion de los pines
GPIO.set_mode(GPIO.BCM)
# Indicamos que el pin es de salida
GPIO.setup(pin, GPIO.OUT)

# Si el modo es "on"
if mode == "on":
  # Encendemos el led
  GPIO.output(pin, GPIO.HIGH)
  print("led on")
else:
  # Apagamos el led
  GPIO.output(pin, GPIO.LOW)
print("led off")