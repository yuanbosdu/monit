# -*- coding: utf-8 -*-
from django.db import models
from rabbitmq.test.consumer import *
import threading

# define the new rabbitmq consumer job
rabbit_consumer = threading.Thread(target=job)
rabbit_consumer.setDaemon(True)  # set it as Daemon
rabbit_consumer.start()
print("start new rabbitmq consumer")
