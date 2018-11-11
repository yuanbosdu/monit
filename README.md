#monit project
###how to boot up the server
nohup gunicorn -c gunicorn.conf.py monit.wsgi:application
###how to restart the server
- find the PID using "ps aux"
- kill -HUP PID
###how to stop the server
- find the PID using "ps aux"
- kill -9 PID
