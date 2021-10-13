from celery import Celery
from .models import MyModel


app = Celery('testProject')

import requests

#
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, debug.s('https://code.tutsplus.com/ru/tutorials/using-celery-with-django-for-background-task-processing--cms-28732'), name='add every 10')

@app.task
def debug(url):
    # return requests.get(url)
    r = requests.get(url)
    new_object = MyModel.objects.create(url=r)
    return new_object.url