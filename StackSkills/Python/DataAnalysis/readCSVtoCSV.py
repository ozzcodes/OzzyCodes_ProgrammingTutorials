import pandas as pd

# The cvs dataset to read
df = pd.read_csv('CrimeStatebyState2.csv')

# Create a new Dataset from original csv to new csv
df['Violent Crime rate'].to_csv('newCSV2.csv')

# display data by using an index
df.set_index('Year', inplace=True)

# Print the first 5 data index points
print(df.head())

df['Violent Crime rate'].to_csv('newCSV2.csv')
