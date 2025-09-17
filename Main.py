import random
import time;
import datetime
import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management Systems")
root.configure(background = 'Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5 relief=RIDGE)
Tops.pack(side=TOP)

MenuFrame = Frame(root, bg='Cadet Blue', bd=10, pady=5 relief=RIDGE)
MenuFrame.pack(side=LEFT)

root.mainloop()