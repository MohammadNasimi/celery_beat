from django.urls import path

from rss.views import rsslist


urlpatterns= [

path("reader/", rsslist.as_view(), name='index')

]