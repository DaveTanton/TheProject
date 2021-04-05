import random
import math
import csv
import tkinter as tk
from tkinter import *

#tkinter framework before adding logic

SWACG = tk.Tk()
SWACG.title("SWACG")
SWACG.geometry("1500x1000")

tfm = Frame(SWACG)

topFrame1 = Frame(tfm, bg="red", width="300",height="200")
tfLabel1 = tk.Label(topFrame1,text="SWAGC")
tfLabel1.pack(fill="both", expand=True)
topFrame1.pack(side ="left")

topFrame2 = Frame(tfm, bg="blue", width="300",height="200")
topFrame2.pack(side ="left")

topFrame3 = Frame(tfm, bg="green", width="300",height="200")
topFrame3.pack(side ="left")

topFrame4 = Frame(tfm, bg="yellow", width="300",height="200")
topFrame4.pack(side ="left")

topFrame5 = Frame(tfm, bg="pink", width="300",height="200")
topFrame5.pack(side ="left")
tfm.pack()

mfm =Frame(SWACG)
mapFrame =Frame(mfm,bg="white",width="1500", height="600")
mapFrame.pack(side="left",fill="both")
mfm.pack()

bfm = Frame(SWACG)
bottomFrame1 = Frame(bfm, bg="red", width="300",height="200")
bottomFrame1.pack(side ="left")

bottomFrame2 = Frame(bfm, bg="blue", width="300",height="200")
bottomFrame2.pack(side ="left")

bottomFrame3 = Frame(bfm, bg="green", width="300",height="200")
bottomFrame3.pack(side ="left")

bottomFrame4 = Frame(bfm, bg="yellow", width="300",height="200")
bottomFrame4.pack(side ="left")

bottomFrame5 = Frame(bfm, bg="pink", width="300",height="200")
bottomFrame5.pack(side ="left")
bfm.pack()

SWACG.mainloop()
