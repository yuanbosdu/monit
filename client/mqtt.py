# -*- encoding:utf-8 -*-
import paho.mqtt.client as mqtt
import time

HOST = '127.0.0.1'
PORT = 61613
USER = 'temp'
PASSWORD = 'temp'

show_promt = 0


def on_connect(client, userdata, flags, rc):
    global show_promt
    print('Connect with result code %s' % str(rc))
    client2.subscribe('client1')
    show_promt = show_promt + 1


def on_message(client, userdata, msg):
    print(client)
    print(msg.topic, str(msg.payload))


client1 = mqtt.Client('123')
client1.username_pw_set(USER, PASSWORD)
client1.on_connect = on_connect
client1.on_message = on_message

client2 = mqtt.Client('456')
client2.username_pw_set('admin', 'password')
client2.on_connect = on_connect
client2.on_message = on_message


client1.connect_async(HOST, PORT, keepalive=60)
client2.connect_async(HOST, PORT, keepalive=60)
client1.loop_start()
client2.loop_start()

while True:
    time.sleep(1)
    if show_promt == 2:
        cmd = input('input message:')
    if cmd == 'quit':
        print('end mqtt')
        client1.loop_stop()
        client2.loop_stop()
        break
    client1.publish('client1', '*'.join((cmd, time.strftime('%H-%M-%S', time.localtime(
        time.time()))
    )))
