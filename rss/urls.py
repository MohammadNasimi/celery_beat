from django.urls import path

from rss.views import rsslistView


urlpatterns= [

path("reader/", rsslistView.as_view(), name='index')

]