#!/usr/bin/python3
import sqlite3

# Define the database Name and connection to be created
conn = sqlite3.connect('test.db')

# Define the cursor for SQLite to grab all information
c = conn.cursor()


# Define a table for the database (SQL language)
def create_table():
    c.execute('CREATE TABLE Example(Language VARCHAR, Version REAL, Skill TEXT)')


# Insert data directly form code
def enter_data():
    c.execute("INSERT INTO Example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO Example VALUES('Python', 3.4, 'Intermediate')")
    c.execute("INSERT INTO Example VALUES('Python', 3.6, 'Expert')")
    conn.commit()  # Commit the data to the Database


# Enter data dynamically through user input
def enter_dynamic_data():
    lang = input("What language? ")
    version = float(input("What version? "))
    skill = input("What skill level? ")

    # Insert input data into database using connection to dynamic data
    c.execute("INSERT INTO Example (Language, Version, Skill) VALUES (?, ?, ?)", (lang, version, skill))

    conn.commit()


# Read from database
def read_from_database():
    # what_skill = input("What skill level to look for? ")
    # what_language = input("What language? ")

    # sql = "SELECT * FROM Example"
    # sql = "SELECT * FROM Example LIMIT 2"
    sql = "UPDATE Example SET Skill = 'Beginner' WHERE Skill = 'Beginner'"

    c.execute(sql)  # Run to make any changes to the database

    print(20 * '#')

    sql = "DELETE FROM Example WHERE Skill = 'Beginner'"

    # for row in c.execute(sql, [what_skill, what_language]):
    for row in c.execute(sql):
        print(row)


# Run call type
read_from_database()

# Close connection
conn.close()
