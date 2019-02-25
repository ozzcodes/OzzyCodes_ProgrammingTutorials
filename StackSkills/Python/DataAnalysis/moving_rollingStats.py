import pandas as pd
import pandas_datareader as wb
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 1, 1)

att = wb.DataReader("T", 'yahoo', start, end)

# Can set describe to your own parameters
describe = att.describe()

# Dataframe standard deviation
print(describe['Open']['std'])

# Get the rolling mean for the specified points (moving average)
att['50MA'] = pd.DataFrame.rolling(att['Close'], 50).mean()
att['10MA'] = pd.DataFrame.rolling(att['Close'], 10).mean()

print(att.tail())

# Create 2 subplots 2 columns, 1 row
fig, axes = plt.subplots(nrows=2, ncols=1)

# Get Standard Deviation
att['50STD'] = pd.DataFrame.rolling(att['Close'], 50).std()
att['50STD'].plot(ax=axes[1], label='50STD')

att['Close'].plot(ax=axes[0], label='Price')
att['50MA'].plot(ax=axes[1], label='50MA')
att['10MA'].plot(ax=axes[1], label='10MA')

plt.legend(loc=4)
plt.show()
