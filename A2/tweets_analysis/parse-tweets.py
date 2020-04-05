#!/usr/bin/env python3
"""parse-tweets.py"""

import sys, json

arg = sys.argv[1]

for line in arg:
    if not line.isspace():
        data = json.loads(line)
        print(data["text"])
