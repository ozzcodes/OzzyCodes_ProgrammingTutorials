from ftplib import FTP
import tkinter as Tk

from guizero import ListBox


def connect():
    text.delete('1.0', Tk.END)
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
c = Tk.Canvas(root, width=800, height=500)
c.pack()
text = Tk.Text(c, borderwidth=10, background='lightgray')
text.pack(side=Tk.RIGHT, expand=True)
cc = Tk.Button(root, text='Connect', command=connect)
cc.pack()
lbox = ListBox(root)
lbox.pack(side=Tk.LEFT, expand=1)
