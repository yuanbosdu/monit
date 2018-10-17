# -*- coding: utf-8 -*-
import serial
import requests

url = 'http://localhost:8000/serial/push/'
mserial = serial.Serial("COM1", 115200)

print(mserial.portstr)

if mserial.is_open:
    print("the serial port has open")
else:
    print("open the serial port now")

while True:
    # text = mserial.readline()
    # print(text)
    payload = {
        'name': 'test',
        'state': 'dangerous',
    }
    res = requests.post(url, data=payload)
    print(res)
    print("end the call")
    break

