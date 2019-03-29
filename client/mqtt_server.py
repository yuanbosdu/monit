#-*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time
import datetime
import pytz
from peewee import *
import random
from playhouse.shortcuts import model_to_dict, dict_to_model

import serial
import time
import json
import threading

HOST = '127.0.0.1'
PORT = 61613
USER = 'admin'
PASSWORD = 'password'
DATABASE = '/opt/monit/db.sqlite3'

global sclient

def on_connect(client, userdata, flags, rc):
    print("Connect with result code %s" % str(rc))
    client.subscribe('mqtt_data')

def on_message(client, userdata, msg):
    print(client)
    print(msg.topic, str(msg.payload))

def start_server_client():
    sclient = mqtt.Client("server_client")
    sclient.username_pw_set(USER, PASSWORD)
    sclient.on_connect = on_connect
    sclient.on_message = on_message

    sclient.connect_async(HOST, PORT, keepalive=60)
    sclient.loop_start()

end = True

while end:
    cmd = None
    # start server client
    start_server_client()

    while True:
        cmd = input("input message:")
        if cmd == 'quit':
            print("end server client")
            sclient.loop_stop()
            end = False
            break


