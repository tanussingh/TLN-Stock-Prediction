#Import Libraries
import tweepy
import numpy as np
import requests
import json
import matplotlib.pyplot as plt
from textblob import TextBlob
from sklearn.svm import SVR
import time

# plt.switch_backend('TkAgg')
#Set up keys
consumer_key= 'lfwX1K8WKvRKiMJbFdAHWasAP'
consumer_secret= 'CdP3aCqeqh0VlxPZMU32yQqYfB81A5fUdLKXuqNXvcjRoFtsJZ'
access_token='1112419514531106818-mfrqvlgd663qHNsvjonH9FMwRo9DeV'
access_token_secret='6Dhqvrwf3TkS832WPvHYYZCUt4SyYN3szy5pnq4GWrdUz'

#Set up twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search('Google')

#Initialize values
threshold=0
pos_sent_tweet=0
neg_sent_tweet=0

#Analyze tweets
for tweet in public_tweets:
    analysis=TextBlob(tweet.text)
    if analysis.sentiment.polarity >= threshold:
        pos_sent_tweet=pos_sent_tweet+1
    else:
        neg_sent_tweet=neg_sent_tweet+1
if pos_sent_tweet>neg_sent_tweet:
    print ("Overall Positive")
else:
    print ("Overall Negative")


# given a date in the format YYYY-MM-DD,
# returns the number of days since January 1, 0000 -ish
def date_to_int(date):
    year = int(date.split('-')[0])
    month = int(date.split('-')[1])
    day = int(date.split('-')[2])

    return (year - 1) * 366 + (month - 1) * 31 + day

# Predict prices of stocks
def predict_prices(symbol, date):
    dates = []
    prices = []
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+symbol+'&apikey=5NI1IIVU2A0YGL2H')
    response_dict = r.json()
    response_dict_improved = response_dict["Time Series (Daily)"]
    for key_date in response_dict_improved:
        price_json = response_dict_improved.get(key_date).get('1. open')
        dates.append(date_to_int(key_date))
        prices.append(price_json)
    dates = np.reshape(dates, (-1, 1))
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_rbf.fit(dates, prices)
    '''
    # Plotting is not necessary in production
    plt.scatter(dates, prices, color='orange', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Company Stock')
    plt.legend()
    plt.show()
    '''
    return svr_rbf.predict([[date]])[0], (dates, prices)
