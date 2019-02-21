import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import pandas.io.data as web

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = (datetime.datetime(2015, 7, 28))

att = web.DataReader('T', 'yahoo', start, end)

print(att.head)
