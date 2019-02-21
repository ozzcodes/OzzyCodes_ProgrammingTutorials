import pandas as pd

# Column name(headers) then list of rows(data content)
starting = {'Col_1': [5, 2, 4, 7],
            'Col_2': [6, 7, 2, 1],
            'Col_3': [10, 4, 8, 3],
            'Col_4': [3, 2, 6, 6],
            'Col_5': [1, 5, 3, 6],
            'Col_6': [10, 7, 9, 5], }

# Create a DataFrame (similar to a spreadsheet layout)
df = pd.DataFrame(starting)
print(df)
# Prints the data types
print(df.dtypes)
# Print out a references point
print(df['Col_1'][0])
print(df.Col_1)
