#!/usr/bin/env python3.6

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

input_file = sys.argv[1]
unique_tweet_total = 2580081

data = pd.read_csv(input_file, sep="\t", header=None, names=['pronouns', 'freq'] )

# normalize the freq column
data['freq'] = data['freq']/unique_tweet_total

data.plot(kind='bar', y='freq', x='pronouns')
plt.savefig('output_mongodb.png')
