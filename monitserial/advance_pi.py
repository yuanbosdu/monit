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

try:
    # mserial = serial.Serial(SERIAL_PORT, SERIAL_BAUD)
    pass
except Exception as err:
    print(err)

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


def push_server_data(surl, data):
    pass
    payload = {
        'name': data['name'],
        'ename': data['ename'],
        'state': data['state'],
    }
    ret = requests.post(surl, data=payload)
    print(ret)


def serial_task():
    pass
    # 每隔10s 串口读取当前设备状态信息
    # 支持设备列表通过get接口获取
    # 串口设备打开
    # 串口设备发送更新命令
    # 设备收集状态信息发回给主机
    # 同步码为uuid字符串

    mdata = dict()
    mdata.update(name='test')
    mdata.update(ename='test')
    mdata.update(state='test')
    push_server_data(url_push, mdata)

    time.sleep(10)


def pi_job():
    print("start pi job")
    while True:
        serial_task()


joblist = list()
t = threading.Thread(target=pi_job)
# t.setDaemon(True)
t.start()
joblist.append(t)


