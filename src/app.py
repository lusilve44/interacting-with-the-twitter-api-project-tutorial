import os
from dotenv import load_dotenv
import tweepy
import requests
import pandas as pd
import numpy as np
import re


# load the .env file variables

load_dotenv()

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

# your app code here

client = tweepy.Client(bearer_token=bearer_token,
consumer_key=consumer_key,
consumer_secret=consumer_secret,
access_token=access_token,
access_token_secret=access_token_secret,
return_type = requests.Response,
wait_on_rate_limit=True)

query = '#100daysofcode (pandas OR python) -is:retweet'
tweets = client.search_recent_tweets(query,tweet_fields = ['lang','author_id','created_at'],max_results=100)

tweets_dict = tweets.json()
tweets_data = tweets_dict.get('data')
df_tweets = pd.DataFrame.from_dict(tweets_data)
print(df_tweets.head(10))
df_tweets.to_csv('coding-tweets.csv')

def word_in_text(word,tweet_text):
    word = word.lower()
    tweet_text = tweet_text.lower()
    result = re.search(word,tweet_text)
    if result != None:
        return True
    else:
        return False

#Alternative way:
# def word_in_text(word,tweet_text):
#     word = word.lower()
#     tweet_text = tweet_text.lower()

#     return (word in tweet_text)


counts_pandas = 0
counts_python = 0

for i in range(len(df_tweets)):
    
    pandas = word_in_text('pandas', df_tweets.iloc[i]['text'])
    python = word_in_text('python', df_tweets.iloc[i]['text'])
    
    if pandas:
        counts_pandas += 1
    if python:
        counts_python += 1

print(f'There are {counts_pandas} tweets that mentioned the word "pandas"')
print(f'There are {counts_python} tweets that mentioned the word "python"')

#Data visualization in explore notebook