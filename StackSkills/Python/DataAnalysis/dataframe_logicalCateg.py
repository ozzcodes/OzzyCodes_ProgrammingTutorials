import pandas_datareader as wb
import datetime
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 1, 1)

att = wb.DataReader("T", 'yahoo', start, end)

print(att.head())
print(70 * '#')

"""
Asking a Logical question and returning column responses
"""
# Is the closing price greater than the opening
att['Daily_Rise'] = att['Close'] > att['Open']

print(att.head())

# Returns a a dataframe - where the below is true
att2 = att[(att['Close'] > att['Open'])]
print(att2.head())

# Returns the difference of high minus low of a day
att['HL'] = att['High'] - att['Low']

# Greater than a dollar return
att3 = att[(att['HL'] > 1)]
print(att3.head())
