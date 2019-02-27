import pandas as pd

# Column name(headers) then list of rows(data content)
starting = {'Col_1': [5, 2, 4, 7, 6, 3],
            'Col_2': [6, 7, 2, 1, 1, 9],
            'Col_3': [10, 4, 8, 3, 9, 5],
            'Col_4': [3, 2, 6, 6, 8, 8],
            'Col_5': [1, 5, 3, 6, 3, 5],
            'Col_6': [10, 7, 9, 5, 1, 6], }

# Create a DataFrame (similar to a spreadsheet layout)
df = pd.DataFrame(starting)

# Prints the first 5 rows of data (helpful with append function)
print(df.head())
# Last 5 values of data (helpful with append function)
print(df.tail())

# print(df)

# Printing a certain column and index
print(df['Col_1'][2])
