'''
1. Read the input file tweets_engagements.csv and explore
'''
import pandas as pd
import numpy as np

tweets = pd.read_csv("data/tweet_engagements.csv")

print(tweets.head())
print(tweets.describe())

