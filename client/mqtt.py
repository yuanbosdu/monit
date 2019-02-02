# -*- encoding:utf-8 -*-
import paho.mqtt.client as mqtt
import time
import datetime
import pytz
from peewee import *
import random
from playhouse.shortcuts import model_to_dict, dict_to_model


HOST = '127.0.0.1'
PORT = 61613
USER = 'temp'
PASSWORD = 'temp'
DATABASE = '/opt/monit/monit/db.sqlite3'

show_promt = 0

# connect to the databasse
db = SqliteDatabase(database=DATABASE)
db.connect()

class BaseModel(Model):

    class Meta:
        database = db


class Device(BaseModel):
    name = CharField(max_length=50)
    desc = TextField()
    address = CharField(max_length=50)
    ctime = DateTimeField()
    mtime = DateTimeField()
    ename = CharField(max_length=50)
    uuid = UUIDField()

    class Meta:
        table_name='zigbee_zigbee'


class DeviceState(BaseModel):
    utime = DateTimeField()
    state = CharField(max_length=50)
    zigbee_id = IntegerField()
    state_type = CharField(max_length=50)

    class Meta:
        table_name = 'zigbee_zigbeestate'


test1 = Device.filter(uuid='b3826b7c-26a3-11e9-8bc0-40a5ef06d51d')[0]
deviceId = test1.id
print(deviceId)

for i in range(10):
    newState = DeviceState.create(
        utime=datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai')),
        zigbee_id=deviceId,
        state=random.randint(1, 10),
        state_type='string',
    )

exit()


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
