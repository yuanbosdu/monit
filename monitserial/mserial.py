# -*- coding: utf-8 -*-
import serial
import requests
import time
import json
import threading

url = 'http://localhost:8000/serial/push/'
url_change = 'http://localhost:8000/serial/change/'
url_get = 'http://localhost:8000/serial/get/'
mserial = serial.Serial("COM1", 115200)

device_list = [
    b'Gas',
    b'Alcohol',
    b'Hall',
    b'Shock',
    b'Pir',
    b'Humidity:',
    b'Taideng',
]

device_name = [
    '气体监测',
    '酒精监测',
    'Hall监测',
    'Shock监测',
    'Pir监测',
    '温湿度监测',
    '台灯',
]

print(device_list)

print(mserial.portstr)

if mserial.is_open:
    print("the serial port has open")
else:
    print("open the serial port now")


lock = threading.Lock()

def serial_push():
    global lock
    while True:
        need_push = False
        r_name = None
        r_name_english = None
        r_state = None

        # lock.acquire()
        text = mserial.readline()
        # lock.release()

        text = text.split()
        print(text)
        if len(text) > 0 and text[0] in device_list:
            r_name_english = text[0]
            r_state = text[-1]
            print(text)
            print(r_name)
            print(r_state)
            print('*' * 10)

            need_push = True

        time.sleep(1)

        if need_push:
            need_push = False
            print(r_name_english)
            payload = {
                'name': device_name[device_list.index(r_name_english)],
                'ename': r_name_english,
                'state': r_state,
            }
            res = requests.post(url, data=payload)
            print(res)
            print("end the call")


joblist = list()
for i in range(10):
    j = threading.Thread(target=serial_push)
    j.setDaemon(True)
    j.start()
    joblist.append(j)

while True:

    # global lock

    print('*' * 10)
    # to check the actions of device
    print("get the actions of device")
    res = requests.get(url_get)
    print(res.json())
    res = res.json()

    print(res)

    if res.get('err') == 'None':
        print('do the action job')
        if res.get('ename', None) == 'Taideng':
            if res.get('newstate') == 'ON':
                print('write 1')
                # lock.acquire()
                mserial.write(b'1')
                # lock.release()
            else:
                print('write 0')
                # lock.acquire()
                mserial.write(b'0')
                # lock.release()
            print("change the taideng state")
    time.sleep(1)
    print('*' * 10)




