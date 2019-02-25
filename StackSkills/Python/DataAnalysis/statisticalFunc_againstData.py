import pandas_datareader as wb
import datetime
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 1, 1)

att = wb.DataReader("T", 'yahoo', start, end)

print(att.head())
print(70 * '#')


# Can set describe to your own parameters
describe = att.describe()

# Describes the changes in the stock during timeframe
print(att.describe)

print(describe['Open'])

# Dataframe standard deviation
print(describe['Open']['std'])
