#!/usr/bin/env python3.6

import pymongo
from pymongo import MongoClient
import sys, json

#dir_file = sys.argv[1]

client = MongoClient('mongodb://localhost:27017/')
db = client['twitter']
collection_tweets = db['tweets']

"""
with open(dir_file, 'r') as f:
    for line in f:
        if not line.isspace():
            data = json.loads(line)

collection_tweets.insert_many(data)
client.close()

post = {"author":"Mei",
        "text":"Yay! My first tweet.",
        }

posts = create_db.posts
result = posts.insert_one(post)

meis_post = posts.find_one({'author':'Mei'})

print(meis_post)

collection_tweets.drop()
"""


print(client.database_names())
