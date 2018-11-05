# -*- coding: utf-8 -*-
import pika
import time
import json

from zigbee.models import Zigbee, ZigbeeAction, ZigbeeState
from rabbitmq.views import mq_push
user = 'guest'
passwd = 'guest'
host = '127.0.0.1'
port = 5672
vhost = '/'
heartbeat = 0
queue = 'monit'


# now make it as a sub thread

def job():
    credentials = pika.PlainCredentials(user, passwd)
    parameters = pika.ConnectionParameters(host, port, vhost, credentials,
                                           heartbeat=heartbeat)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    channel.basic_consume(callback, queue=queue, no_ack=True)

    print('[x] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def callback(ch, method, properities, body):
    print("[x] Received %r" % json.loads(body))
    body = json.loads(body)
    print(body.get('english', None))
    print(body.get('newstate', None))

    # first get the zigbee state
    mZigbee = Zigbee.objects.get(english=body['english'])
    print(mZigbee)

    mZigbeeState = ZigbeeState.objects.filter(zigbee=mZigbee).order_by('-utime')[0]
    print(mZigbeeState)
    mZigbeeAction = ZigbeeAction.objects.filter(zigbee=mZigbee).order_by('-ctime')[0]
    print(mZigbeeAction)

    if mZigbeeState is None or mZigbeeAction is None:
        return

    if mZigbeeState.state != mZigbeeAction.newstate or mZigbeeState.utime < mZigbeeAction.ctime:
        print("push the body to the queue again")
        mq_push(json.dumps(body))
    elif mZigbeeAction.newstate == mZigbeeState.state and mZigbeeState.utime > mZigbeeAction.ctime:
        print("delete the body from the queue")
        mZigbeeAction.done = True
        mZigbeeAction.save()
    else:
        print("push the body to the queue again")
        mq_push(json.dumps(body))
    time.sleep(1)

