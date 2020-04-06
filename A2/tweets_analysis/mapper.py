#!/usr/bin/env python3
"""mapper.py"""

import sys
import re
import json

tweet_text = []
for line in sys.stdin:
    if not line.isspace():
        data = json.loads(line)
        if not 'retweeted_status' in data:
            tweet_text.append(data["text"])

# declare list of pronouns for search    
pronouns = ["han","hon","den","det","denna","denne","hen"]

# input comes from STDIN (standard input)
for line in tweet_text:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # use regrex to search for words with special characters
    regrex = re.compile('[^a-öA-Ö]')
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1

        # split the words by special characters and match it with elements in pronouns.
        splitted = regrex.split(word.lower())
        for s_words in splitted:
            if s_words in pronouns:
                print('{}\t{}'.format(s_words, 1))

