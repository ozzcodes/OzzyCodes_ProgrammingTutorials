#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect('LXF.sqlite')
c = conn.execute("SELECT count(*) from sqlite_master")

for row in c:
    print(row)

# The SQLite schema of sqlite_master:
'''
sqlite> .schema sqlite_master
CREATE TABLE sqlite_master (
  type text,
  name text,
  tbl_name text,
  rootpage integer,
  sql text
);
sqlite> PRAGMA TABLE_INFO(sqlite_master);
0|type|text|0||0
1|name|text|0||0
2|tbl_name|text|0||0
3|rootpage|integer|0||0
4|sql|text|0||0
'''
