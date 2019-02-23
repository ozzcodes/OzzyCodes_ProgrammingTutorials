import pandas as pd

# The cvs dataset to read
df = pd.read_csv('CrimeStatebyState2.csv')

# Create a new Dataset from original csv to new csv
df['Violent Crime rate'].to_csv('newCSV2.csv')

# display data by using an index
df.set_index('Year', inplace=True)

df['Violent Crime rate'].to_csv('newCSV2.csv')

# The cvs dataset to read
df = pd.read_csv('newCSV2.csv')

# Print the first 5 data index points
print(df.head())

# The cvs dataset to read with a column index specified
df = pd.read_csv('newCSV2.csv', index_col=0)
# Print the first 5 data index points
print(df.head())

# Add the Label headers to the csv file to be printed
df = pd.read_csv('newCSV2.csv', names=['Date', 'Violent Crime rate'], index_col=0)
print(df.head())

df.to_csv('newCSV3.csv')
df.to_csv('newCSV4.csv', header=False)
