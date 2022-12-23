from bs4 import BeautifulSoup
import requests
# import rest framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
# other app import
from datetime import date
# rss app 
from rss.models import news
# import celery 
from celery import shared_task
from task.celery import app

from rss.serializers import newsSerializer


@app.task
def create_news(entries):
        for entry in range(5):
            title = entries[entry].title.text
            updated = entries[entry].updated.text
            summary = entries[entry].summary.text
            link = entries[entry].link['href']
            news.objects.create(title= title , updated = updated,summary = summary,link = link)

class rsslistView(ListAPIView):
    serializer_class = newsSerializer
    permission_classes =[IsAuthenticated]
     
    def get_queryset(self):
        queryset =news.objects.all()
        queryset = queryset.order_by('updated')  # use -data ASC and data DESC
        
        return queryset

  
    def get(self, request, format=None):
        url = requests.get('https://realpython.com/atom.xml')
        soup = BeautifulSoup(url.content ,'xml')
        entries = soup.find_all('entry')
        create_news.delay(entries)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data,status= status.HTTP_200_OK)