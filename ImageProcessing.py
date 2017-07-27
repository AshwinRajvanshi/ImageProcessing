import cv2
import numpy
from Tkinter import *
from tkFileDialog   import askopenfilename      
from Tkinter import Tk, Label, Button

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Image Processing")
        self.label.pack()

        self.hi_button = Button(master, text="hey ", command=self.hi)
        self.hi_button.pack()

        
        self.File_open= Button(master, text="select Image", command=self.fileopen)
        self.File_open.pack()
        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


        
    def hi(self):
        print("hi!")


    def fileopen(self):
        name= askopenfilename() 
        print name
        img=cv2.imread(name) 
        print"I got %d bytes from this file." % len(name)
        retval,threshold1=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
        grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        retval2,threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
        gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
        cv2.imshow('real',img)
        cv2.imshow('thresh',threshold1)
        cv2.imshow('Gray2',threshold2)
        cv2.imshow('gaus',gaus)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    

root = Tk()
my_gui = MyGUI(root)
root.mainloop()
