from celery import Celery
from celery.schedules import crontab

from .models import MyModel


app = Celery('testProject')

import requests


@app.task
def debug(*args):

    for x in args:
        r = requests.get(x)
        new_object = MyModel.objects.create(x=r)
        return new_object.x