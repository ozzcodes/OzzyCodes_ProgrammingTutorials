from ftplib import FTP
import tkinter as Tk


def connect():
    text.delete('1.0', END)
    selection = lbox.curselection()
    site = lbox.get(selection[0])
    connection = FTP(site)
    connection.login("anonymous", "aMail@gmail.com")
    print("Connected to %s" % site)
    files = []
    files = connection.nlst()

    for f in files:
        text.insert('1.0', f)
        text.insert('1.0', "\n")

    connection.close()
    text.focus()


root = Tk()
root.title('A simple FTP Client')
c = Canvas(root, width=800, height=500)
c.pack()
text = Text(c, borderwidth=10, background='lightgray')
text.pack(side=RIGHT, expand=True)
cc = Button(root, text='Connect', command=connect)
cc.pack()
lbox = ListBox(root)
lbox.pack(side=LEFT, expand=1)
