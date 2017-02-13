.#!/usr/local/bin/python3

'''
    *   Twitter Bot for Python 3.6 Version 1.0
    *   Created by Abdulrahman Tolba on 2/07/17.
    *   Copyright © 2017 Abdulrahman Tolba. All rights reserved.
    '''

# Importing tweepy to easily access the Twitter API
import tweepy
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener, Stream

CONSUMER_KEY = 'YOUR CONSUMER KEY HERE'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET HERE'
ACCESS_TOKEN = 'YOUR ACCESS TOKEN KEY HERE'
ACCESS_SECRET = 'YOUR ACCESS SECRET KEY HERE'

# auth will authorize our account with our unique consumer and access keys.
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# api will connect to the Twitter API with auth.
api = tweepy.API(auth)


class twitterBot(StreamListener):
    def on_data(self, raw_data):
        try:
            isRetweeted = raw_data.lower().split('"retweeted":')[1].split(',"possibly_sensitive"')[0].replace(",", "")
            # Accessing the tweet's text
            tweetText = raw_data.lower().split('"text":"')[1].split('","source":"')[0].replace(",", "")
            # Accessing the username of tweet author
            userName = raw_data.lower().split('"screen_name":"')[1].split('","location"')[0].replace(",", "")
            # Accessing the tweet ID number
            tweetId = raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", "")
            
            retweet(tweetId)
            print("Tweet was retweeted successfully! Tweet URL: ")
            print("https://twitter.com/" + userName  + "/status/"  + tweetId + "\n")
            
            return True
        except Exception as e:
            # If an error occurs, tweepy will print the error message to the screen
            print(str(e))
            pass

def on_error(self, status_code):
    print("Error: " + status_code)

def retweet(tweetId):
    try:
        api.retweet(tweetId)
    except Exception as e:
        print(str(e))
        pass

def fav(tweetId):
    try:
        api.create_favorite(tweetId)
    except Exception as e:
        print(str(e))
        pass

def tweetPost(tweetText):
    try:
        api.update_status(status=tweetText)
    except Exception as e:
        print(str(e))
        pass

# Retweet any tweet with these speciifc phrases
track_words = ["",""]
# Retweet every tweet from this accounts (user ID's from gettwitterid.com)
follow_acc = [""]

print("Running...")
try:
    twt = Stream(auth, twitterBot())
    twt.filter(track=track_words)
except Exception as e:
    print(str(e))
pass
