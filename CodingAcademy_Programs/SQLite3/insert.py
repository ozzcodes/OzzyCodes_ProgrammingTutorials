from SQLite3.sqliteConnect import conn

conn.execute("INSERT INTO ISSUES (NUMBER, YEAR, COMMENTS) VALUES "
             "(202,2015, 'Best issue ever!')")
conn.execute("INSERT INTO ISSUES (NUMBER, YEAR, COMMENTS) VALUES "
             "(203,2015, 'Best Linux Format issue ever!')")
conn.commit()

conn.execute("INSERT INTO LXFISSUES (ID, NUMBER, YEAR, COMMENTS) VALUES"
             "(0,202,2015,'Best issue ever!')")
conn.execute("INSERT INTO LXFISSUES (ID, NUMBER, YEAR, COMMENTS) VALUES"
             "(1,203,2015, 'Best Linux Format issue ever!')")
conn.commit()
