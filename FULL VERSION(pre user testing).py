'''
    author: Zeph Frear Hanson
    date: 15/11/2021
    title: full version pre testing
    description: full version of the code
'''

import image
from tkinter import *
from tkinter import messagebox

trstock = 3
trbcount = 0
trscount = 0

whstock = 12
whbcount = 0
whscount = 0

shstock = 8
shbcount = 0
shscount = 0

image_list = ['1.gif', '2.gif', '3.gif']
text_list = ['summer hoodie', 'tracksuit', 'winter hoodie']
current = 0
img_obs = []

#function for buying summer hoodie
def buysh():
    global shbcount
    shbcount += 1
    label1.config(text=f'you have bought {shbcount} item')
    global shstock
    shstock -= 1
    label2.config(text=f'{shstock} left in stock')
    if shstock == 0:
        messagebox.showinfo("no","no more stock!")

#function for restocking summer hoodie
def sellsh():
    global shscount
    shscount += 1
    label3.config(text=f'you have restocked this item {shscount} times')
    global shstock
    shstock += 1
    label2.config(text=f'{shstock} left in stock')

#function for buying winter hoodie
def buywh():
    global whbcount
    whbcount += 1
    label1.config(text=f'you have bought {whbcount} item')
    global whstock
    whstock -= 1
    label2.config(text=f'{whstock} left in stock')
    if whstock == 0:
        messagebox.showinfo("no","no more stock!")

#function for restocking winter hoodie
def sellwh():
    global whscount
    whscount += 1
    label3.config(text=f'you have restocked this item {whscount} times')
    global whstock
    whstock += 1
    label2.config(text=f'{whstock} left in stock')

#function for buying tracksuit
def buytr():
    global trbcount
    trbcount += 1
    label1.config(text=f'you have bought {trbcount} item')
    global trstock
    trstock -= 1
    label2.config(text=f'{trstock} left in stock')
    if trstock == 0:
        messagebox.showinfo("no","no more stock!")

#function for restocking tracksuit
def selltr():
    global trscount
    trscount += 1
    label3.config(text=f'you have restocked this item {trscount} times')
    global trstock
    trstock += 1
    label2.config(text=f'{trstock} left in stock')

#function to change image
def move(delta):
    global current, img_obs

    if not (0 <= current + delta < len(image_list)):
        messagebox.showinfo('End', 'No more image.')
        return
    current += delta
    label['text'] = text_list[current]
    label.config(image = img_obs[current])



#make window
root = Tk()
root.title("Sports uniform shop")
root.geometry("800x800+0+0")
root.configure(bg="white")


#title
FONT = ("Comic Sans MS", "16", "bold")

lbl_title = Label(root, text="Sports uniform shop",
                  bg="black",
                  fg="white", font=FONT,)

lbl_title.pack()


#image gallery
for i in range(len(image_list)):
    img_obs.append(PhotoImage(file=image_list[i]))

label = Label(root, compound= TOP, image=img_obs[0])
label.pack()

frame = Frame(root)
frame.pack()





#product type
lbl_type = Label(root, text="Tracksuit")
lbl_type.place(x=360, y=450)

#buy button
custom_button = Button(root, text="buy", command=buytr)
custom_button.place(x=360, y=468)

#restock button
custom_button = Button(root, text="restock", command=selltr)
custom_button.place(x=360, y=492)

#entry for restocking
label3 = Label(root)
label3.place(x=360, y=550)

#bought message
label1 = Label(root)
label1.place(x=360, y=568)

#total stock message
label2 = Label(root)
label2.place(x=360, y=586)





#product type
lbl_type = Label(root, text="Winter Hoodie")
lbl_type.place(x=520, y=450)

#buy button
custom_button = Button(root, text="buy", command=buywh)
custom_button.place(x=520, y=468)

#restock button
custom_button = Button(root, text="restock", command=sellwh)
custom_button.place(x=520, y=492)

#entry for restocking
label3 = Label(root)
label3.place(x=360, y=550)

#bought message
label1 = Label(root)
label1.place(x=360, y=568)

#total stock message
label2 = Label(root)
label2.place(x=360, y=586)


#product type
lbl_type = Label(root, text="Summer Hoodie")
lbl_type.place(x=100, y=450)

#restock button
custom_button = Button(root, text="restock", command=sellsh)
custom_button.place(x=100, y=468)

#buy button
custom_button = Button(root, text="buy", command=buysh)
custom_button.place(x=100, y=492)

#entry for restocking
label3 = Label(root)
label3.place(x=360, y=550)

#bought message
label1 = Label(root)
label1.place(x=360, y=568)

#total stock message
label2 = Label(root)
label2.place(x=360, y=586)





#button to display previous image
btn = Button(frame, text='Previous picture',
               command=lambda: move(-1))
btn.pack(side=LEFT)

#button to display next image
btn_pre = Button(frame, text='Next picture',
               command=lambda: move(+1))
btn_pre.pack(side=LEFT)

move(0)
root.mainloop()

    
