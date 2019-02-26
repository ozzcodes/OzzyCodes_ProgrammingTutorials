import pandas as pd
import urllib.request

# Read in an HDF file
df = pd.read_hdf('hdfstore.h5', 'd1')
print(df.head())

# Convert a file to JSON
df.to_json('example_json.json')

# Read the JSON file
df2 = pd.read_json('example_json.json')
print(df2.head())

# Retrieve the url request from blockchain's website and api request
depth_json = urllib.request.urlopen('https://api.blockchain.info/charts/transactions-per-second?timespan=5weeks'
                                    '&rollingAverage=8hours&format=json').read()
depth_df = pd.read_json(depth_json)
print(depth_json)
