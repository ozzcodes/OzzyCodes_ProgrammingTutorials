import pandas_datareader as wb
import datetime
from matplotlib import style


style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 1, 1)

att = wb.DataReader("T", 'yahoo', start, end)

print(att.head())
print(70 * '#')
att['Open_original'] = att['Open']
att['Open'] = att['Open'] / 10

print(att.head())

att['High_minus_low'] = att['High'] - att['Low']
print(att.head())
