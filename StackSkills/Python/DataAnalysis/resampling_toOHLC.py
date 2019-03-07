import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

tickers = ['AAPL']
start_date = '2012-03-01'
end_date = '2019-03-01'

df = pdr.DataReader(tickers, 'morningstar', start_date, end_date)

df.sort_values('Date', inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print(df.head())
