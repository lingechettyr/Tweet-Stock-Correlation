#Import relevant APIs
import numpy as np
import pandas as pd
import tweepy as tw
import yfinance as yf
import sys
import tweepy
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
from tweepy import OAuthHandler
from tweepy import API
from sklearn.linear_model import LinearRegression

key = 'knEh6mj2ALzzf5Tt4kwlAyWfP'
secret = 'sO6uHy1pkEhlIfG8fwjahTx2wG6I3ttT2DdKOBDm2uyTzTrr7f'
access_token = '885961353730588673-ARCKXmaFuTQHglu4oy50H7UPIbwu7Wf'
access_secret = 'F7KaeDlR0A0ZRBk2ThmkOq77HO5EmqUUpKQ4wPlcFPKl6'

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

end_date = date.today()
days_prior = input("Enter the number of days to retrieve market data (max 7 days, min 2 days):  ")
start_date = end_date - timedelta(days=int(days_prior))
weekno = start_date.weekday()
tickers = ['TSLA','AAPL', 'FB']
correlation = {}
perChange = []

if weekno < 5 and int(days_prior) <= 7 and int(days_prior) >= 2:
    stock_data = yf.download(tickers, start=start_date, end=end_date, progress=False, group_by='ticker')
    for tick in tickers:
        percent_change = (((stock_data[tick]['Close'])[-1] - (stock_data[tick]['Close'])[str(start_date)])/
            (stock_data[tick]['Close'])[str(start_date)])*100
        perChange.append(round(abs(percent_change), 2))
        correlation[tick] = round(abs(percent_change), 2)
elif weekno >=5:
    sys.exit("Input leads to a date on the weekend. Exiting...")
elif int(days_prior) > 7 or int(days_prior) < 2:
    sys.exit("Input does not match constraints. Exiting...")

public_tweets = []
tweetsDict = {}
count = 0
counter = 0
tweetCount = []
maxID = 0
tickers = ['$TSLA','$AAPL', '$FB']
for tick in tickers:
    while counter < 10:
        if maxID > 0:
            public_tweets = api.search(q = tick, count = 10, since = start_date, until = end_date, max_id = maxID)
        else:
            public_tweets = api.search(q = tick, count = 10, since = start_date, until = end_date)
        count += len(public_tweets)
        maxID = public_tweets[len(public_tweets) - 1].id
        counter += 1
    tweetCount.append(count)
    tweetsDict[tick] = count - 9 #Account for replicate tweets from using maxID
    counter = 0
    count = 0
    maxID = 0
print (tweetsDict)

x = np.array(perChange).reshape((-1,1))
y = np.array(tweetCount)
lr = LinearRegression().fit(x,y)
lr.fit(x,y)
corr = np.corrcoef(perChange, tweetCount)[0,1]
r2 = lr.score(x,y)
pred = lr.predict(x)
plt.scatter(x,y)
plt.plot(x, pred, color = 'red')
print (corr)
print (r2)
