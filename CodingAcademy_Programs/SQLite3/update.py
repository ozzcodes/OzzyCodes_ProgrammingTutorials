from SQLite3.sqliteConnect import conn

conn.execute("UPDATE ISSUES set YEAR = '2016' where YEAR='2015'")
conn.commit()
print("Total number of rows updated:", conn.total_changes)
