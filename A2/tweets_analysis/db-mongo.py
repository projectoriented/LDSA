#!/usr/bin/env python3.6
"""db-mongo.py"""

"""This script will load in unique tweet data to MongoDB with each tweet as a single document"""


from pymongo import MongoClient
import sys, json

dir_file = sys.argv[1]

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Initiate + write a database
db = client['twitter']

# Declare name of collections
collection_tweets = db.collection_tweets

# Parse the tweet JSON files and grab only the texts (tweets)
tweet = []
with open(dir_file, 'r') as f:
    for line in f:
        if not line.isspace():
            data = json.loads(line)
            tweet.append(data['text'])

# take the unique tweets
tweet = set(tweet)

# Load into the database; each tweet is its own document in collection_tweets.
for text in tweet:
    collection_tweets.insert_one({'tweet':text})
