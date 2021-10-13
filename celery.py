import os

from celery import Celery
# from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testProject.settings')

app = Celery('testProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'repeat' : {
        'task' : 'myapp.tasks.debug',
        'schedule' : 10.0,
        'args' : 'https://code.tutsplus.com/ru/tutorials/using-celery-with-django-for-background-task-processing--cms-28732'
    }
}

app.conf.timezone = 'UTC'


# if __name__ == '__main__':
#     app.start()
