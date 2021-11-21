'''
    author: Zeph Frear Hanson
    date: 8/11/2021
    title: Component 1(GUI)
    description: Skeleton for what the program will end up looking like.
'''

from tkinter import *
from tkinter import messagebox

class Protitle:
    def __init__(self, parent):
        FONT = ("Comic Sans MS", "24", "bold")

        lbl_title = Label(parent, text="Sports uniform shop",
                          bg="black",
                          fg="white", font=FONT,
                          padx= 80, pady= 24,)

        lbl_title.pack()


if __name__=="__main__":
    root = Tk() #creates grpahics object
    root.title("Sports uniform shop")
    root.geometry("800x800+0+0")
    label = Protitle (root)
    root.mainloop()

