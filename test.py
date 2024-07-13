#! /usr/bin/python

# https://www.youtube.com/watch?v=4zhZVFBnSsI&t=276s
# # apt-get install python3-pip
# pip install adafruit_dht # (senza sudo)
# pip install simple-http-server

import sys
# import Adafruit_DHT
import time
from simple_http_server import route, server
from datetime import datetime
import random

@route("/")
def index():
    HTML_CONTENT = """<!DOCTYPE html><html lang="it"><head>"""
    HTML_CONTENT = HTML_CONTENT + """<meta charset="UTF-8"><META HTTP-EQUIV="Pragma" CONTENT="no-cache"><META HTTP-EQUIV="Expires" CONTENT="-1"></head>"""
    HTML_CONTENT = HTML_CONTENT + """<body><h1>simple_http_server</h1>"""
    HTML_CONTENT = HTML_CONTENT + """http://locahost:8080/</body></html>"""
    return (HTML_CONTENT)
@route("/json")
def index():
    HTML_CONTENT =  """{"temperature":"0", "humidity":"0"}"""
    return (HTML_CONTENT)

server.start(port=8080)