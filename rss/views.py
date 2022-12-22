from bs4 import BeautifulSoup
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rss.models import news

class rsslistView(APIView):

    def get(self, request, format=None):
        url = requests.get('https://realpython.com/atom.xml')
        soup = BeautifulSoup(url.content ,'xml')
        entries = soup.find_all('entry')
        data = {}
        for entry in range(5):
            title = entries[entry].title.text
            updated = entries[entry].updated.text
            summary = entries[entry].summary.text
            link = entries[entry].link['href']
            create_news = news.objects.create(title= title , updated = updated,summary = summary,link = link)
            data('entry').append(entries[entry])
        return Response(data,status=status.HTTP_400_BAD_REQUEST)