
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
import time
import dht11

dht_instance = dht11.DHT11(pin = 24)

while True:
    result = dht_instance.read()
    if result.is_valid():
        temperature = result.temperature
        humidity = result.humidity
        print ("temperature is :",str(temperature))
        print ("humidity is :",str(humidity))


    time.sleep (5)

    else:
        print ("not a valid number")

    time.sleep(5)
