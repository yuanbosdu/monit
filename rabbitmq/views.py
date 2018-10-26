from django.shortcuts import render

# Create your views here.
import pika
import time


def mq_push(body):
    credentials = pika.PlainCredentials('guest', 'guest')
    parameter = pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameter)
    channel = connection.channel()

    channel.queue_declare(queue='monit')
    channel.basic_publish(
        exchange='',
        routing_key='monit',
        body=body
    )
    print("the push body is %s" % body)

    connection.close()