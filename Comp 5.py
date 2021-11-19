'''
    author: Zeph Frear Hanson
    date: 14/11/2021
    title: Component 4(error for stock)
    description: once stock on item has reached 0 an error message pops up
'''

from tkinter import *
from tkinter import messagebox

shstock = 8
bcount = 0
scount = 0


def buy():
    global bcount
    bcount += 1
    label1.config(text=f'you have bought {bcount} item')
    global shstock
    shstock -= 1
    label2.config(text=f'{shstock} left in stock')
    if shstock == 0:
        messagebox.showinfo("no","no more stock!")


#make window
root = Tk()
root.title("Sports uniform shop")
root.geometry("800x800+0+0")
root.configure(bg="white")

#bought message
label1 = Label(root)
label1.grid(column=0, row=1)

#total stock message
label2 = Label(root)
label2.grid(column=0, row=2)

#buy button
custom_button = Button(root, text="buy", command=buy)
custom_button.grid(column=1, row=0)
