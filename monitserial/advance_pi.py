#-*- coding:utf-8 -*-
import serial
import requests
import time
import json
import threading

IOT_SERVER = 'http://172.22.116.53'
IOT_PORT = '8000'
SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_BAUD = 115200

url = IOT_SERVER + ':' + IOT_PORT
url_push = url + '/serial/push/'
url_change = url + '/serial/change/'
url_get = url + '/serial/get/'
