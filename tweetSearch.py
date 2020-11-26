import tweepy

key = 'knEh6mj2ALzzf5Tt4kwlAyWfP'
secret = 'sO6uHy1pkEhlIfG8fwjahTx2wG6I3ttT2DdKOBDm2uyTzTrr7f'
access_token = '885961353730588673-ARCKXmaFuTQHglu4oy50H7UPIbwu7Wf'
access_secret = 'F7KaeDlR0A0ZRBk2ThmkOq77HO5EmqUUpKQ4wPlcFPKl6'

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

public_tweets = []
tweetsDict = {}
count = 0
tickers = ['TSLA', 'AAPL', 'FB'] #Took out cashtag symbol

for tick in tickers:
    while count < 100: #Change condition to see if we have reached the tweet pull limit
        public_tweets += api.search(q = tick, count = 100, since = '2020-11-25', until = '2020-11-25')
        count += 1
    tweetsDict[tick] = count
    count = 0
    
count = 0
for tweets in public_tweets:
    count += 1

print (count)
