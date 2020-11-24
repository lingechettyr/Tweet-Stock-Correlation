#Import relevant APIs
import numpy as np
import pandas as pd
import tweepy as tw
import matplotlib.pyplot as plt

#Twitter Authentication
from tweepy import OAuthHandler
from tweepy import API

apiKey = 'sUY1UAhfmauoDAqodxPJCmE1d'
apiSecret = 'nRrYuBn8X1MauIFfyznAXdwdLsTcVReytlIUpsfjiI2GncodX0'
accessToken = '3295318197-LMzVBdXwZPbIgJU8Fd0ksjT8mEOES2HRYC2J2ha'
accessSecret = 'RgqkfaXowXGk1JaKs0jTOIvGVjZbGnL32bsPk4DuzohBf'

auth = OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessSecret)
api = API(auth)

#Searching and Storing


