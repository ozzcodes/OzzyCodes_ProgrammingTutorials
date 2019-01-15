#!/usr/bin/python3
import sqlite3
import tkinter
from tkinter import *
import tkinter.scrolledtext as ST
import sys


def callBack():
    print("value is", variable.get())
    text.delete('1.0', END)
    myText = "Table name:" + variable.get()
    text.insert('insert', myText)


# First argument is the database name
database = sys.argv[1]

conn = sqlite3.connect(database)
c = conn.cursor()

root = Tk()
canvas = Canvas(root, width=810, height=600)
canvas.pack()

text = ST.ScrolledText(canvas, width=35, height=20, borderwidth=0)
text.pack()

# This is a dummy list of tables
listOfTables = {"sqlite_master",
                "one",
                "two",
                "three"}

variable = StringVar(root)
variable.set("sqlite_master")  # the default value
w = OptionMenu(root, variable, *listOfTables)
w.pack()

Button(root, text='Quit', command=root.quit)\
    .pack(side=BOTTOM, anchor=SE)
Button(root, text='OK', command=callBack).pack(side=TOP,
                                               anchor=SE)

mainloop()
