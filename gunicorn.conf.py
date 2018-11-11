import multiprocessing
import sys
sys.path.append('/opt/monit')

bind = "127.0.0.1:8080"
workers = 2
errorlog = '/opt/log/gunicorn.error.log'
#accesslog = '/opt/log/gunicorn.access.log'
#loglevel = 'debug'
proc_name = 'gunicorn_monit'
