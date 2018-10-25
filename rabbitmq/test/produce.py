# -*- coding: utf-8
import pika
import time

credentials = pika.PlainCredentials('guest', 'guest')
parameter = pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials, 100, heartbeat_interval=0)
connection = pika.BlockingConnection(parameter)
channel = connection.channel()

channel.queue_declare(queue='monit')

for i in range(100):
    channel.basic_publish(exchange='',
                        routing_key='monit',
                        body='Hello World')
    time.sleep(5)

print("[x] Sent 'Hello World!'")
connection.close()