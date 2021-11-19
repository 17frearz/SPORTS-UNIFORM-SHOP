'''
    author: Zeph Frear Hanson
    date: 10/11/2021
    title: Component 2 version 2
    description: Displays images from a folder when
    option ondropdown is clicked.
'''
from tkinter import *

root = Tk() #creates grpahics object
root.title("Sports uniform shop")
root.geometry("800x800+0+0")



image_names = ["summerhoodie.gif","tracksuit.gif","winterhoodie.gif"]
image_list = []  #what will hold the PhotoImage object


#name_lbl.config(image=img)
image = ("/image/tracksuit.gif")  #image must be gif format
img = PhotoImage(image)


for i in range(len(image_names)):
    image_list.append(PhotoImage(file = "image/" + image_names[i])) 

name_lbl = Label(root, image = image_list[0]) #0 is first PhotoImage object
name_lbl.pack()

#dropdown menu
sv = StringVar()
sv.set('Summer hoodie')
items = ['Summer hoodie','Winter hoodie','Tracksuit']
om = OptionMenu(root,sv,*items)
om.pack()
