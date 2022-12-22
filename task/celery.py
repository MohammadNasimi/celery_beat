from celery import Celery

app = Celery('rss')

app.config_from_object('django.conf:settings',namespace = 'CELERY')

app.conf.beat_schedule ={
    'rss_task_every_5_min':{
        'rss' : 'rss.views.create_news',
        'schedule': 60*5
        
    }
}