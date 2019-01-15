import sqlite3
import sys

# First argument is the database name
database = sys.argv[1]

# Second argument is the table name
tableName = sys.argv[2]

conn = sqlite3.connect(database)
c = conn.cursor()
query = "select * from " + tableName + "where 1=0"
c.execute(query)

# This will be empty because of the query
rs = c.fetchall()
field_names = [r[0] for r in c.description]

for f in field_names:
    print("*", f)
