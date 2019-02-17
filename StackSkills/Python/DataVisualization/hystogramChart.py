#!/usr/bin/python3

import matplotlib.pyplot as plt

# Create a list of data
test_scores = [92, 76, 77, 90, 85, 46, 99, 68, 77, 34, 56, 87, 65, 90, 100, 77, 78, 89]

x = [x for x in range(len(test_scores))]
plt.bar(x, test_scores)

plt.show()

# Create bins for the Histogram to refer too
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(test_scores, bins, histtype='bar', cumulative=True, rwidth=0.8)

plt.show()
