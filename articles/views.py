from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from .models import Article,Importance
from rest_framework import generics
from rest_framework import permissions
from .serializers import ArticleSerializer, ImportanceSerializer
from django.db.models import Q
from rest_framework.response import Response
# Create your views here.

first_article = "http://thenationonlineng.net/whats-wrong-with-administration-of-criminal-justice-act-2/"
importance_url = "https://lawpavilion.com/blog/the-administration-of-criminal-justice-act-2015-acja/"

def get_page(info):
    page = requests.get(info)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    main_page = soup.find('div', class_="single-the-content")
    article = soup.find_all('p')
    articles =[]
    mydict = {}
    count = 1
    my_objects = list(Article.objects.all())
    if not my_objects:
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
    
    else:
        for x in article:
            text = x.get_text().lower()
        # text = text.count("Part")
            if 'part' in text:
                articles.append(x.get_text())
                Nm = "ACJA ACT PART "+ str(count)
                # save_story = Article(name=Nm, content=x.get_text())
                # save_story.save()
                # count= count + 1
        return articles
    



    
def get_importance_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    main_page = soup.find(id="post-content")
    article = main_page.find_all('p')
    articles =[]
    mydict = {}
    count = 1
    my_objects = list(Importance.objects.all())
    if not my_objects:
        for x in article:
            text = x.get_text().lower()
        # text = text.count("Part")
            if len(text)>30:
                articles.append(x.get_text())
                Nm = "IMPORTANCE "+ str(count)
                save_story = Importance(name=Nm, content=x.get_text())
                save_story.save()
                count= count + 1
        return articles
        
    else:
        for x in article:
            text = x.get_text().lower()
        # text = text.count("Part")
            if len(text)>30:
                articles.append(x.get_text())
                # Nm = "IMPORTANCE "+ str(count)
                # save_story = Importance(name=Nm, content=x.get_text())
                # save_story.save()
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
    

class ImportanceAPIView(generics.ListAPIView):
    queryset = Importance.objects.all()
    serializer_class = ImportanceSerializer
    

def importance_page(request):
    
    importance = get_importance_page(importance_url)
    template = "importance.html"
    context = {
        'importance':importance,
    }
    
    return render(request, template, context) 
