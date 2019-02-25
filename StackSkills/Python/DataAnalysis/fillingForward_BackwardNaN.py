import pandas_datareader as wb
from pandas import DataFrame as df
import datetime
from matplotlib import style
from statistics import mean


# Created function for moving average
def moving_average(data):
    return mean(data)


# Random simple algorithm
def fancy_this(data):
    return mean(data) + mean(data) + 5


# Define a style to use
style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 1, 1)

att = wb.DataReader("T", 'yahoo', start, end)
# Can set describe to your own parameters
describe = att.describe()

# Get the rolling mean for the specified points (moving average)
att['50MA'] = df.rolling(att['Close'], 50).mean()
att['10MA'] = df.rolling(att['Close'], 10).mean()

# Get Standard Deviation
att['50STD'] = df.rolling(att['Close'], 50).std()

# using rolling function with apply
att['MA_with_apply'] = df.rolling(att['Close'], 50).apply(moving_average, raw=False)
att['apply'] = df.rolling(att['Close'], 50).apply(fancy_this, raw=False)
print(att.head())

# Fill forward function
# att.fillna(method='bfill', inplace=True)

# Replace the NaN values with a specified value
# att.fillna(value=-99999, inplace=True)

one_pct = len(att) * 0.01
att.fillna(value=-99999, inplace=True)
print(att)

if att.isnull().values.sum() > 1:
    print('Found remaining NA, more than 1% is not a number!')

att.fillna(value=-99999, inplace=True, limit=9000)
if att.isnull().values.sum() > 1:
    print('Found remaining NA, more than 1%+9000 is not a number!')
