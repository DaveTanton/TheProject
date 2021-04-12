import random
import math
import csv
import SWACG
from tkinter import *, ttk
from PIL import ImageTk, Image, ImageGrab

def save_as_png(widget,file_name):
    x=myWin.winfo_rootx()+widget.winfo_x()
    y=myWin.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()
    ImageGrab.grab(bbox=(x,y,x1,y1)).save(file_name+".png")

    #maybe a big save function that takes the map, playassets and other info and creates a PDF might be beyond me at presnt

myWin = Tk()
myWin.title("SWACG")
myWin.iconbitmap("Art/icon.ico")#check me
myWin.geometry("1500x600")

cv = Canvas(myWin,width=1500,height=600)
cv.place(x=0,y=0)

image1 =ImageTk.PhotoImage(file="Art/test"+str(SWACG.randomRoll(1,3))+".png")
cv.create_image(0,0,image=image1,anchor=NW)

testPlayer=8 #testing only
testRegion=3 #testing only
plst=SWACG.assetCreator(testRegion,testPlayer) #testing only
flst=SWACG.mapPosition(plst,testPlayer) #testing only

img_lst=[]
for i in range (len(flst)):
    PPH = ImageTk.PhotoImage(file="Art/PPH.png")
    cv.create_image((flst[i][1][0]),(flst[i][1][1]),image=PPH)
    cv.create_text((flst[i][1][0]),(flst[i][1][1])+40,text=flst[i][0]["name"],font="Impact",fill="white")
    img_lst.append(PPH)

#saves an image 500ms after the call testing only
myWin.after(250, lambda:save_as_png(cv,"texty"))
myWin.mainloop()
