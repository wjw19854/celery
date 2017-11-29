from celery import Celery

app = Celery('tasks', backend='rpc://')

app.conf.broker_url = 'redis://localhost:6379/0'

@app.task
def add(x,y):
    return x + y

