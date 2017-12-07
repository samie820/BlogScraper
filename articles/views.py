from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from .models import Article
from rest_framework import generics
from rest_framework import permissions
from .serializers import ArticleSerializer
from django.db.models import Q
from rest_framework.response import Response
# Create your views here.

first_article = "http://thenationonlineng.net/whats-wrong-with-administration-of-criminal-justice-act-2/"


def get_page(info):
    page = requests.get(info)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    main_page = soup.find('div', class_="single-the-content")
    article = soup.find_all('p')
    articles =[]
    mydict = {}
    count = 1
    for x in article:
        text = x.get_text().lower()
        # text = text.count("Part")
        if 'part' in text:
            articles.append(x.get_text())
            Nm = "ACJA ACT PART "+ str(count)
            save_story = Article(name=Nm, content=x.get_text())
            save_story.save()
            count= count + 1
    return articles
    

def index(request):
    
    article = get_page(first_article)
    template = "index.html"
    context = {
        'article':article,
    }
    
    return render(request, template, context)
    
class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    
    