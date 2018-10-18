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
    b'Humidity',
]

device_name = [
    b'气体检测',
    b''
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
    r_state = None
    text = mserial.readline()
    text = text.split()
    print(text)
    if text[0] in device_list:
        r_name = text[0]
        r_state = text[-1]
        print(text)
        print(r_name)
        print(r_state)
        print('*' * 10)

        need_push = True

    time.sleep(1)
    payload = {
        'name': r_name,
        'state': r_state,
    }
    if need_push:
        need_push = False
        res = requests.post(url, data=payload)
        print(res)
        print("end the call")

