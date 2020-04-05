#!/usr/bin/env python3
"""parse-tweets.py"""

import sys, json

arg = sys.argv[1]

with open(arg, 'r') as f:
    for line in f:
        if not line.isspace():
            data = json.loads(line)
            print(data["text"])
