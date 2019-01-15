from SQLite3.sqliteConnect import conn

conn.execute("DELETE FROM ISSUES where ID='2'")
conn.commit()
print("Total number of rows deleted:", conn.total_changes)
