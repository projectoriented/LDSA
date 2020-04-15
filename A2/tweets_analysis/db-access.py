#!/usr/bin/env python3.6

from pymongo import MongoClient
import re
from bson.code import Code

client = MongoClient('mongodb://localhost:27017/')
db = client['twitter']
collection_tweets = db.collection_tweets
unique_tweet_count = db.collection_tweets.count() # fetch total doc. count in the collection

mapper = Code("""
                function () {
                    var pronouns = ["han","hon","den","det","denna","denne","hen"];
                    pronouns.sort();
                    var tweet = this.tweet;
                    var regrex = new RegExp(/[\d+\W+]/i);
                    splitted_array = tweet.split(regrex);

                    for (var j = 0; j < splitted_array.length; j++){
                    new_word = splitted_array[j].toLowerCase();
                    if (pronouns.includes(new_word)){
                        emit(new_word, 1)
                        }
                    }
                }
                """)

reducer = Code("""
                function (key, values) {
                    var total = 0;
                    for (var i = 0; i < values.length; i++) {
                        total += values[i];
                    }
                    return total;
                }
                """)

result = collection_tweets.map_reduce(mapper, reducer, "pronouns")
for doc in result.find():
    print(doc)
