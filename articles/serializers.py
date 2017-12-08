from rest_framework import serializers
from .models import Article, Importance


class ArticleSerializer(serializers.ModelSerializer):
    
    #Serializing all articles
    class Meta:
        model = Article
        fields = ('id','name','content')
        


class ImportanceSerializer(serializers.ModelSerializer):
    
    #Serializing all articles
    class Meta:
        model = Importance
        fields = ('id','name','content')