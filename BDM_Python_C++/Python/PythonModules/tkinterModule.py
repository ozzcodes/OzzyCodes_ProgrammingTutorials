import tkinter as tk
from tkinter import *

# Run from terminal to generate a window
wind = Tk()
btn = Button()
btn.pack()
btn['text'] = 'Hello Everyone!'


def click():
    print('You just clicked me!')


btn["command"] = click
