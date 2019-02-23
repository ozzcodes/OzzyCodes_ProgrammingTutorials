import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import pandas_datareader as pdr

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = (datetime.datetime(2015, 7, 28))

# Use symbol automatically (att = AT&T
att = pdr.DataReader("T", "yahoo", start, end)

print(att.head())

# att['Adj Close'].plot()
# att['High'].plot()
# att['Low'].plot()

att[['High', 'Low']].plot()
plt.legend()
plt.show()
