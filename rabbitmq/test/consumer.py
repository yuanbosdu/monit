# -*- coding: utf-8 -*-
import pika
import time

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('127.0.0.1',
                                       5672, '/', credentials, heartbeat=0)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='monit')


def callback(ch, method, properities, body):
    print("[x] Received %r" % body)


channel.basic_consume(callback, queue='monit', no_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
