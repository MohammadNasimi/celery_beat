from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','task.settings')
app = Celery('task')

app.config_from_object('django.conf:settings',namespace = 'CELERY')

app.autodiscover_tasks()
app.conf.beat_schedule ={
    'task_task_every_5_min':{
        'task' : 'rss.views.create_news',
        'schedule': 60*5
        
    }
}