from django.db import models

# Create your models here.

class news (models.Model):
    title = models.TextField(max_length=200)
    updated = models.DateTimeField()
    summary = models.TextField(max_length=200)
    link = models.URLField(max_length=128,db_index=True,unique=True,blank=True)