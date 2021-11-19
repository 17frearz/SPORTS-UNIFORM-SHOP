'''
    author: Zeph Frear Hanson
    date: 8/11/2021
    title: Component 2 version 1(Image gallery)
    description: Displays image with buttons on either side to go from
    one image to the next.
'''

import image
#import tkinter
from tkinter import *
from tkinter import messagebox

image_list = ['1.gif', '2.gif', '3.gif']
text_list = ['summer hoodie', 'tracksuit', 'winter hoodie']
current = 0
#---photo image objects---------
img_obs = []



def move(delta):
    global current, img_obs

    if not (0 <= current + delta < len(image_list)):
        messagebox.showinfo('End', 'No more image.')
        return
    current += delta
    #image = image.open(image_list[current])
    #photo = imageTk.PhotoImage(image)
    label['text'] = text_list[current]
    label.config(image = img_obs[current])
    #label.photo = photo


root = Tk()
root.geometry("800x800+0+0")

for i in range(len(image_list)):
    img_obs.append(PhotoImage(file=image_list[i]))
    5

label = Label(root, compound= TOP, image=img_obs[0])
label.pack()

frame = Frame(root)
frame.pack()

btn = Button(frame, text='Previous picture',
               command=lambda: move(-1))
btn.pack(side=LEFT)

btn_pre = Button(frame, text='Next picture',
               command=lambda: move(+1))
btn_pre.pack(side=LEFT)

move(0)

root.mainloop()
