from rest_framework import serializers
from rss.models import news

class newsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = news
        fields = ('id', 'title', 'updated','summary', 'link')
        read_only_fields = ('id', 'title', 'updated','summary', 'link')
