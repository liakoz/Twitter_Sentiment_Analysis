import tweepy
from textblob import TextBlob
import unicodecsv as csv

consumer_key= 'nphtJ5GIXWRVyTRhNuRCV9WmY'
consumer_secret= 'AwPdKgiSJURy7j0aSuIWZemZrTEdmaUZP8oiQDT9sYonicDJY6'

access_token= '1280450850452889600-axAbwiPLT43w0vVsLCQxx2eIbiqqGZ'
access_token_secret= 'Mon1ebEC5c3sUly6R8PTbLJKUXOGvDiDmFOiL729XybwM'

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api= tweepy.API(auth)

public_tweets = tweepy.Cursor(api.search,q='Joe Biden',count=10,lang='en').items(2)


with open('SentimentAnalyzer.csv','w',newline='',encoding='utf-8') as file:
    writer= csv.writer(file)
    writer.writerow(["Sentiment","Tweet"])
    for tweet in public_tweets:
        analysis=TextBlob(tweet.text)
        print(analysis.words)
        if analysis.sentiment.polarity >= 0:
           writer.writerow(["positive",tweet.text])
        else:
            writer.writerow(["negative",tweet.text])
            
            
                    
    
