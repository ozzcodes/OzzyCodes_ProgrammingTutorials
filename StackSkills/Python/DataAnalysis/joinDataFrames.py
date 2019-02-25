import pandas as pd

df1 = pd.DataFrame({'Temp': [75, 73, 72, 76],
                    'Humidity': [20, 45, 32, 42],
                    'Precipitation': [0, 0, 0, 1], })

df2 = pd.DataFrame({'Temp': [75, 73, 72, 76],
                    'Wind': [33, 35, 37, 23],
                    'Cloudy': [1, 0, 1, 1], })

# Merge two dataframe and bring together on a single 'like' column name
print(pd.merge(df1, df2, on='Temp'))

main_users = pd.DataFrame({'Username': ['James', 'Sanjay', 'Karl', 'Kelly', 'Carl'],
                           'Password': ['P@ssw0rd', '1234', 'pass', 'pw', '2gjhggj7'],
                           'Join_Date': ['Jan', 'Feb', 'Jan', 'March', 'April'], })

forum_users = pd.DataFrame({'Username': ['James', 'Sanjay', 'Karl', 'Kelly'],
                            'Post_Count': [500, 521, 76, 999],
                            'User_Status': [0, 1, 0, 2], })

print(pd.merge(main_users, forum_users, on='Username'))

# Create an actual/ useful column name instead of automated
main_users.set_index('Username', inplace=True)
forum_users.set_index('Username', inplace=True)

joined = main_users.join(forum_users)
print(joined)


"""
Example using the joining as merging
"""
main_users = pd.DataFrame({'Username': ['James', 'Sanjay', 'Karl', 'Kelly', 'Carl'],
                           'Password': ['P@ssw0rd', '1234', 'pass', 'pw', '2gjhggj7'],
                           'Join_Date': ['Jan', 'Feb', 'Jan', 'March', 'April'], })

forum_users = pd.DataFrame({'Username': ['James', 'Sanjay', 'Karl', 'Kelly'],
                            'Post_Count': [500, 521, 76, 999],
                            'User_Status': [0, 1, 0, 2], })

merged = pd.merge(main_users, forum_users, on='Username')
merged.set_index('Username', inplace=True)
print(merged)


merged = pd.merge(main_users, forum_users, on='Username', how='outer')
merged.set_index('Username', inplace=True)
print(merged)
