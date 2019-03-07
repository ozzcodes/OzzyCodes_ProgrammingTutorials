import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

df = pd.read_pickle('df.pickle')
df.sort_values('Date', inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print(df.head())


# Using resampling (D = day; 3 Days = 3D) --> PandaDocs
df2 = df.resample('3D').mean()
print(df2.head())

# Using resampling (M = month; 1 Month = 1M) --> PandaDocs
df3 = df.resample('1M').mean()
print(df3.head())

df4 = df.resample('12M').mean()
print(df4.head())

df4['TotalVolume'].plot()
df3['TotalVolume'].plot()
df2['TotalVolume'].plot()
df['TotalVolume'].plot()
plt.show()
