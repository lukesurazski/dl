#!/usr/bin/env python

"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    #e = [np.e]
    #sum = np.sum(x)
    #y = np.power(e,x)
    #y_sum = np.sum(y)
    #r = np.divide(y,y_sum)
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)


print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
