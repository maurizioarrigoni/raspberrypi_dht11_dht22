#! /usr/bin/python

# https://www.youtube.com/watch?v=4zhZVFBnSsI&t=276s
# installare apt install python-pip
# installare libreria con 'pip install adafruit_dht' senza sudo

import sys
import Adafruit_DHT
import time

sensor = 22
gpio = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

if humidity is not None and temperature is not None:
        while True:
                try:
                        print('')
                        print('Temperatura: {0:0.1f}*C'.format(temperature, humidity))
                        temp='{0:0.1f}'.format(temperature, humidity)
                        hum='{1:0.1f}'.format(temperature, humidity)
                        output = "{\"temperature\":\"" + temp + "\", \"humidity\":\"" + hum+ "\"}"
                        print(output)
                        print('Umidità: {1:0.1f} %'.format(temperature, humidity))
                        time.sleep(2)
                except KeyboardInterrupt:
                        sys.exit(1)

else:
        print('Impossibile leggere il sensore')
        sys.exit(1)
