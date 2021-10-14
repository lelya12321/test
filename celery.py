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
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'repeat' : {
        'task' : 'myapp.tasks.debug',
        'schedule' : 10.0,
        'args' : ['https://russianblogs.com/article/33401559299/', 'https://docs.djangoproject.com/en/3.2/topics/db/queries/']
    }
}

app.conf.timezone = 'UTC'


