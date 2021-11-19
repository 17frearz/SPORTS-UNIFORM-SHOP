'''
    author: Zeph Frear Hanson
    date: 10/11/2021
    title: Component 4(buy and selling)
    description: Buttons for buying and selling stock
'''

import random
from tkinter import *

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

def sell():
    global scount
    scount += 1
    label3.config(text=f'you have restocked this item {scount} times')
    global shstock
    shstock += 1
    label2.config(text=f'{shstock} left in stock')

    




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


#restock button
custom_button = Button(root, text="restock", command=sell)
custom_button.grid(column=2, row=0)

#entry for restocking
label3 = Label(root)
label3.grid(column=0, row=3)






