#!/usr/bin/env python3
"""parse-tweets.py"""

import sys, json
import re

arg = sys.argv[1]


data=[]
with open(arg, 'r') as f:
    for line in f:
        if not line.isspace():
            data.append(json.loads(line)['text'])

data = set(data)
for x in data:
    print(x)
