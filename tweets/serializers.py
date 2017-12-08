from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    
    #Serializing all articles
    class Meta:
        model = Tweet
        fields = ('id','name','tweets', 'positive_remark', 'negative_remark')
        


