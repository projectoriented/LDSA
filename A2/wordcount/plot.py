#!/usr/bin/env python3.6

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("part-r-00000", sep="\t", header=None, names=["alphabet","freq"])
data.plot(kind='bar', y='freq', x='alphabet')
plt.savefig('output.png')
