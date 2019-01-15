from SQLite3.sqliteConnect import conn

c = conn.execute("SELECT * from ISSUES;")
for record in c:
    print(record)
