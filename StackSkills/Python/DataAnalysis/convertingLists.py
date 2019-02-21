import datetime
import pandas_datareader as pdr
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = (datetime.datetime(2015, 7, 28))

# Use symbol automatically (att = AT&T)
att = pdr.DataReader("T", "yahoo", start, end)

print(att.head())


highs = att['High'].tolist()
# Get the last price of 'High'
print(highs[-1])


highz = att['High']
print(highz[-10])
