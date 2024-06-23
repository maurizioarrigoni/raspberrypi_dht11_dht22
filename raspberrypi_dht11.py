#! /usr/bin/python

# https://www.youtube.com/watch?v=4zhZVFBnSsI&t=276s
# # apt-get install python3-pip
# pip install adafruit_dht # (senza sudo)
# pip install simple-http-server

import sys
import Adafruit_DHT
import time
from simple_http_server import route, server
from datetime import datetime

@route("/")
def index():
    sensor = 11
    gpio = 4
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    HTML_CONTENT = """<!DOCTYPE html><html lang="it"><head>"""
    HTML_CONTENT = HTML_CONTENT + """<meta charset="UTF-8"><META HTTP-EQUIV="Pragma" CONTENT="no-cache"><META HTTP-EQUIV="Expires" CONTENT="-1"></head><body>"""
    HTML_CONTENT = HTML_CONTENT + """<h1>raspi3 + DHT11"""
    if humidity is not None and temperature is not None:
        HTML_CONTENT = HTML_CONTENT + """<h1>Temperatura: """ + '{0:0.1f}*C'.format(temperature, humidity) + """</h1>"""
        HTML_CONTENT = HTML_CONTENT + """<h1>Umidità: """ + '{1:0.1f} %'.format(temperature, humidity) + """</h1>"""
    else:
        HTML_CONTENT = HTML_CONTENT + """<h1>Temperatura e Umidità: N/A</h1>"""
    HTML_CONTENT = HTML_CONTENT + """</body></html>"""
    return (HTML_CONTENT)

server.start(port=8080)