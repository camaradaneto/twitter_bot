#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import random
import tweepy
import time
from os import environ


# In[2]:


def get_quotes():
    with open('meu_arquivo.json') as f:
        quotes_json = json.load(f)
    return quotes_json


# In[3]:


def get_random_quote():
    quotes = get_quotes()
    random_quote = random.choice(quotes)
    return random_quote


# In[4]:


def create_tweet():
    quote = get_random_quote()
    tweet = """
            {}
            ~{}
            """.format(quote[0], quote[1])
    return tweet


# In[5]:


CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


# In[6]:


def  tweet_quote():
    interval = 86401
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    while True:
        tweet = create_tweet()
        api.update_status(tweet)
        time.sleep(interval)


# In[7]:


if __name__ == "__main__":
    tweet_quote()

