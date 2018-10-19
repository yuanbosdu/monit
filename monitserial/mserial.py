# -*- coding: utf-8 -*-
import serial
import requests
import time

url = 'http://localhost:8000/serial/push/'
mserial = serial.Serial("COM1", 115200)

device_list = [
    b'Gas',
    b'Alcohol',
    b'Hall',
    b'Shock',
    b'Pir',
    b'Humidity:',
]

device_name = [
    '气体监测',
    '酒精监测',
    'Hall监测',
    'Shock监测',
    'Pir监测',
    '温湿度监测',
]

print(device_list)

print(mserial.portstr)

if mserial.is_open:
    print("the serial port has open")
else:
    print("open the serial port now")

while True:
    need_push = False
    r_name = None
    r_name_english = None
    r_state = None
    text = mserial.readline()
    text = text.split()
    print(text)
    if text[0] in device_list:
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
            'english': r_name_english,
            'state': r_state,
        }
        res = requests.post(url, data=payload)
        print(res)
        print("end the call")

