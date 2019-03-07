import pandas as pd
import urllib.request
import matplotlib.pyplot as plt


# On Quandl website, right-click on a dataset download to csv button and
# copy link address for pulling data via url
def pickle_data():
    read = urllib.request.urlopen('https://www.quandl.com/api/v3/datasets/FINRA/FNSQ_AAPL.csv?api_key'
                                  '=NxkJbC84Wsa3PsVWiAbN')
    df = pd.read_csv(read)

    print(df.head())
    df.to_pickle('df.pickle')


# pickle_data()

df = pd.read_pickle('df.pickle')

# Sort data by the 'Date' value in dataset
df.sort_values('Date', inplace=True)
df.set_index('Date', inplace=True)
df = df['TotalVolume']
print(df.head())

df.plot()
plt.show()

df = pd.read_pickle('df.pickle')
print(df.head())
df.sort_values('ShortVolume', inplace=True)
print(df.head())
