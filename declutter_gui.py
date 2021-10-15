# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 17:16:41 2021

@author: Charissa
"""

from tkinter import *
import cv2
from PIL import Image

root = Tk()
canvas = Canvas(root, width = 300, height = 300)
#creating label widget
title = Label(root, text = "Declutter").grid(row=0, column=0)
author = Label(root, text = "Made by Charissa, Jun Guang and Kieran from Team Rocket 22").grid(row=1, column=0)
instruction = Label(root, text = "Please upload your bedroom picture below").grid(row=2, column=0)


def uploadbutton():
    file = Label(root, text = "Please enter filename with extension: ").grid(row=4, column=0)
    file1 = Entry(root).grid(row=4, column=1)
    def filename():
        print(file1.get())
    def displayimage():
        img = PhotoImage(file= filename())
        canvas.create_image(20,20, anchor=NW, image=img).grid(row=6, column=0)
    enter = Button(root,text = "Enter", command = displayimage).grid(row= 5, column= 0)
    
    
def takephoto():
    camera = cv2.VideoCapture(0)
    
myButton1 = Button(root,text = "Click here to upload photo", command = uploadbutton, padx = 30, pady = 10, fg= "blue").grid(row=3, column=0)
myButton2 = Button(root,text = "Click here to take photo", command = takephoto,padx = 30, pady = 10, fg= "blue").grid(row=3, column=1)

    
quitbutton = Button(root, text='Quit', command=root.quit).grid(row=10, column= 1)

#show on screen
#myLabel.pack()

root.mainloop()

