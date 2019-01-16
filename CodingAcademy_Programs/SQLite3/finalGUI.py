#!/usr/bin/python3
from tkinter import *
import sqlite3
import tkinter.scrolledtext as ST
import sys

# First argument is the database name
database = sys.argv[1]

conn = sqlite3.connect(database)
c = conn.cursor()

root = Tk()
canvas = Canvas(root, width=810, height=600)
canvas.pack()

text = ST.ScrolledText(canvas, width=35, height=20, borderwidth=0)
text.pack()


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


c.execute("SELECT name FROM sqlite_master WHERE type='table'")
listOfTables = {'sqlite_master': 0}

for record in c:
    # print(record[0])
    listOfTables[record[0]] = 0

variable = StringVar(root)
variable.set("sqlite_master")  # the default value
w = OptionMenu(root, variable, *listOfTables)
w.pack()

Button(root, text='Quit', command=root.quit) \
    .pack(side=BOTTOM, anchor=SE)
Button(root, text='OK', command=callBack) \
    .pack(side=TOP, anchor=SE)

mainloop()
conn.close()
