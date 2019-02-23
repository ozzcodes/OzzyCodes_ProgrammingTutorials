import pandas as pd
import urllib.request
import pickle
import time

# Retrieve the url request from blockchain's website and api request
depth_json = urllib.request.urlopen('https://api.blockchain.info/charts/transactions-per-second?timespan=1weeks'
                                    '&rollingAverage=8hours&format=json').read()
depth_df = pd.read_json(depth_json)
# print(depth_json)

# Convert data into a pickle file
depth_df.to_pickle('pickle.pickle')

# Read the pickle file out to console
newdf = pd.read_pickle('pickle.pickle')
print(newdf)

"""
Using the Pickle library instead of the Panda's library
"""
# Using the pickle library
# Pickle allows you to save ANY OBJECT
pickle_out = open('newdf.pickle', 'wb')
pickle.dump(newdf, pickle_out)
pickle_out.close()

# Read the pickle binary file
pickle_in = open('newdf.pickle', 'rb')
super_cool = pickle.load(pickle_in)
print(super_cool)
print(super_cool.head())


# Compare time for pickle to run vs pandas
start = time.time()
depth_df.to_pickle('pickle.pickle')
newdf = pd.read_pickle('pickle.pickle')
print(time.time() - start)


start = time.time()
pickle_in = open('newdf.pickle', 'rb')
super_cool = pickle.load(pickle_in)
print(time.time() - start)
