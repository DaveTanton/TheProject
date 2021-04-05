import random
import math
import csv
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

def randomRoll(min,max):
    num = random.randint(min,max)
    return num

SWACG = tk.Tk()
SWACG.title("SWACG")
SWACG.geometry("1500x1000")

tfm = Frame(SWACG)

topFrame1 = Frame(tfm, bg="red", width="300",height="200")
# logo/title
topFrame1.pack(side ="left")

topFrame2 = Frame(tfm, bg="blue", width="300",height="200")
# spacer
topFrame2.pack(side ="left")

topFrame3 = Frame(tfm, bg="green", width="300",height="200")
# user input data
topFrame3.pack(side ="left")

topFrame4 = Frame(tfm, bg="yellow", width="300",height="200")
# user input data
topFrame4.pack(side ="left")

topFrame5 = Frame(tfm, bg="pink", width="300",height="200")
# user input data
topFrame5.pack(side ="left")
tfm.pack()

mfm = Frame(SWACG)
mapFrame =Frame(mfm,width="1500", height="600")
#make this a fuction once the nesting is worked out
fileNum=str(randomRoll(1,3))
test=Image.open("Art/test"+fileNum+".png")
testPic=ImageTk.PhotoImage(test)
testPicLabel = tk.Label(mfm,image=testPic)
testPicLabel.image = testPic
testPicLabel.place()
mapFrame.pack(side="left",fill="both")
mfm.pack()

bfm = Frame(SWACG)
bottomFrame1 = Frame(bfm, bg="red", width="300",height="200")
#spacer
bottomFrame1.pack(side ="left")

bottomFrame2 = Frame(bfm, bg="blue", width="300",height="200")
#spacer
bottomFrame2.pack(side ="left")

bottomFrame3 = Frame(bfm, bg="green", width="300",height="200")
#save options
bottomFrame3.pack(side ="left")

bottomFrame4 = Frame(bfm, bg="yellow", width="300",height="200")
#reset buttons
bottomFrame4.pack(side ="left")

bottomFrame5 = Frame(bfm, bg="pink", width="300",height="200")
#reset buttons
bottomFrame5.pack(side ="left")
bfm.pack()

SWACG.mainloop()
