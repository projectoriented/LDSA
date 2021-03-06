#!/usr/bin/env python3.6

from pymongo import MongoClient
import re
from bson.code import Code
import pprint

client = MongoClient('mongodb://localhost:27017/')
db = client['twitter']
collection_tweets = db.collection_tweets
unique_tweet_count = db.collection_tweets.count() # fetch total doc. count in the collection

#pronouns = ["han","hon","den","det","denna","denne","hen"] # pronouns to search for in each tweet
#pronouns.sort()

"""
for x in pronouns:
    counter = 0
    regrex = re.compile(r"[\W \w]?\b" + x + r"\b[\W \w]?", re.IGNORECASE) # powerful regrex to match any special characters/alphabets/numbers flanking the pronouns

    # Use regrex on MongoDB's find() method and process it further with a loop to get all matches within a tweet.
    for posts in collection_tweets.find({'tweet': {'$regex': regrex }}):
        counter += len(regrex.findall(posts['tweet']))
    print('{}\t{}'.format(x, counter))

print('unique_tweet_count\t{}'.format(unique_tweet_count))
"""

mapper = Code("""
                function () {
                    var pronouns = ["han","hon","den","det","denna","denne","hen"];
                    pronouns.sort();
                    var tweet = this.tweet;

                    for (var i = 0; i < pronouns.length; i++){
                        var replace = "[\\W \\w]?\\b" + pronouns[i] + "\\b[\\W \\w]?";
                        var regrex = new RegExp(replace, "ig")
                        var num_a = [];
                        var num_n = 0;
                        if (tweet.match(regrex) == null) {
                            num_n = 0;
                        } else {
                            num_a.push(tweet.match(regrex));
                            emit(pronouns[i], num_a.length);
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
