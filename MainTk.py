import random
import math
import csv
import SWACG
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

#use frames for general area the grids inside the frames for prescion
#lession 11 and lesson 46 ,64
#exe files lesson 40
def clear():
   region_name_box.delete(0,END)
   players_box.delete(0,END)

def clear_name():
   sector_name_box.delete(0,END)

def rolls():
   sector = sector_name_box.get()
   region=int(region_name_box.get())
   planets=int(players_box.get())+1

   planetAssets=SWACG.assetCreator(region,planets)
   assetLst = SWACG.mapPosition(planetAssets, planets)

   sector_name_output = Label(myWin,text=sector)
   sector_name_output.grid(row=5,column=0)
   for i in range(len(assetLst)):
      output = Label(myWin, text=assetLst[i])
      output.grid(row=6+i,column=0,sticky=W)

myWin = Tk()
myWin.title("SWACG")
myWin.iconbitmap("Art/icon.ico")#check me
myWin.geometry("400x200")

sector_name_label = Label(myWin,text="Sector Name").grid(row=0,column=0,padx=5,sticky = E)
region_name_label = Label(myWin,text="Region").grid(row=1,column=0,padx=5,sticky = E)
players_label = Label(myWin,text="Players").grid(row=2,column=0,padx=5,sticky = E)

sector_name_box = Entry(myWin)
region_name_box = Entry(myWin)
players_box = Entry(myWin)

sector_name_box.grid(row=0,column=1,pady=5)
region_name_box.grid(row=1,column=1,pady=5)
players_box.grid(row=2,column=1,pady=5)

add_button = Button(myWin,text="Generate",padx=42,command=rolls)
add_button.grid(row=3,column=0)

clear_button = Button(myWin,text="clear",padx=42,command = clear)
clear_button.grid(row=3,column=1)

clear_button_name = Button(myWin,text="clear",padx=30,command = clear_name)
clear_button_name.grid(row=0,column=2)

myWin.mainloop()
