#! /usr/bin/python

# https://www.youtube.com/watch?v=4zhZVFBnSsI&t=276s
# # apt-get install python3-pip
# pip install adafruit_dht # (senza sudo)
# pip install simple-http-server

import sys
import Adafruit_DHT
import time
from simple_http_server import route, server

@route("/")
def index():
    sensor = 11
    gpio = 4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    #response = 'Temperatura: {0:0.1f}*C'.format(temperature, humidity) +'</br>' + 'Umidità: {1:0.1f} %'.format(temperature, humidity)
    HTML_CONTENT = """<!DOCTYPE html><html lang="it"><head><meta charset="UTF-8"><title></title></head><body>"""
    HTML_CONTENT = HTML_CONTENT + """<h1>raspi3 with DHT11 temperature & humidity sensor</h1>"""
    HTML_CONTENT = HTML_CONTENT + """<h1>Temperatura: """ + '{0:0.1f}*C'.format(temperature, humidity) + """</h1>"""
    HTML_CONTENT = HTML_CONTENT + """<h1>Umidità: """ + '{1:0.1f} %'.format(temperature, humidity) + """</h1>"""
    HTML_CONTENT = HTML_CONTENT + """</body></html>"""
    return (HTML_CONTENT)

server.start(port=8080)