import tweepy
import pandas as pd
import os

# Twitter API credentials
API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# Set up Tweepy authentication
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def fetch_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang='en').items(count)
    data = [[tweet.text] for tweet in tweets]
    df = pd.DataFrame(data, columns=['text'])
    return df

# Fetch and save tweets
tweets_df = fetch_tweets("customer service", count=500)
tweets_df.to_csv('data/raw/twitter_data.csv', index=False)
print("Tweets collected and saved to data/raw/twitter_data.csv")