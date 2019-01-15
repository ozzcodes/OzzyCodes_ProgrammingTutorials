
from SQLite3.gui import variable, text, END, c


def callBack():
    print('Value is', variable.get())
    text.delete('1.0', END)
    tableName = variable.get()
    myText = "Table name:" + tableName
    text.insert('insert', myText + '\n')
    text.insert('insert', "** FIELD NAMES **\n")

    # Get desired Data
    query = "select * from" + tableName + "where 1=0"
    c.execute(query)

    # This will be empty because of the query
    rs = c.fetchall()
    field_names = [r[0] for r in c.description]
    for f in field_names:
        text.insert('insert', '\t' + f + '\n')


listOfTables = {'sqlite_master': 0}

c.execute("SELECT name FROM main.sqlite_master WHERE type='table';")
for record in c:
    # print(record[0])
    listOfTables[record[0]] = 0
