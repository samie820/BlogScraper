from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    
    #Serializing all articles
    class Meta:
        model = Article
        fields = ('id','name','content')