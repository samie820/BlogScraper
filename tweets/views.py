from django.shortcuts import render
from .models import Tweet
from .TwitterClient import main
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import permissions
from .serializers import TweetSerializer
from rest_framework.response import Response
# Create your views here.
# Create your views here.


def get_sentiment(name):
    ptweets, ntweets, positive_rate, negative_rate = main(name)
    name_lower = name.lower()
    my_objects = list(Tweet.objects.filter(name__startswith=name_lower))
    if not my_objects:
        for tweet in ptweets:
        # text = text.count("Part")
            p_name = name_lower+" Positive"
            save_tweet = Tweet(name=p_name, tweets=tweet, positive_remark=positive_rate, negative_remark=negative_rate)
            state_p = save_tweet.save()
        for tweet in ntweets:
        # text = text.count("Part")
            n_name = name_lower+" Negative"
            save_tweet = Tweet(name=n_name, tweets=tweet, positive_remark=positive_rate, negative_remark=negative_rate)
            state_n = save_tweet.save()
        return state_p, state_n
        
    else:
        return True
    


class AllisonTweetAPIView(generics.ListAPIView):
    query = 'diezani allison madueke'
    tweet_sent = get_sentiment(query)
    queryset = Tweet.objects.filter(name__startswith=query)
    serializer_class = TweetSerializer
    

class DasukiTweetAPIView(generics.ListAPIView):
    query = 'Dasuki'
    tweet_sent = get_sentiment(query)
    queryset = Tweet.objects.filter(name__startswith=query)
    serializer_class = TweetSerializer
    


class OlisaTweetAPIView(generics.ListAPIView):
    query = 'Olisa Metuh'
    tweet_sent = get_sentiment(query)
    queryset = Tweet.objects.filter(name__startswith=query)
    serializer_class = TweetSerializer



class YakubuTweetAPIView(generics.ListAPIView):
    query = 'Olisa Metuh'
    tweet_sent = get_sentiment(query)
    queryset = Tweet.objects.filter(name__startswith=query)
    serializer_class = TweetSerializer
    