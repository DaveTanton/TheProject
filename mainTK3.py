import random
import math
import csv
import SWACG
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image,ImageGrab

def card_data(assetlist):
    #MAYBE A CLASS
    global card_frame
    frame_lst=[]
    for e in range(len(assetLst)):
        card_frame = LabelFrame(myWin,text="planet card")
        name_label = Label(myWin, text="planet name: " + assetLst[e][0]["name"])
        vp_label = Label(myWin, text="VP:"+ str(assetLst[e][0]["vp"]))
        lr_label = Label(myWin, text="Location rewards:")
        for i in range(len(assetLst[e][0]["location rewards"])):
            for k, v in assetLst[e][0]["location rewards"][i].items():
                asset = k, v
                lr_asset = Label(myWin, text=asset)
        so_label = Label(myWin, text="Standard Objective cards:")
        for i in range(len(assetLst[e][0]["Standard Objectives cards"])):
            asset = assetLst[e][0]["Standard Objectives cards"][i]
            so_asset = Label(myWin, text=asset)
        co_label = Label(myWin, text="Campaign Objectives cards:")
        for i in range(len(assetLst[e][0]["Campaign Objectives"])):
            asset = assetLst[e][0]["Campaign Objectives"][i]
            co_asset = Label(myWin, text=asset)
        sto_label = Label(myWin, text="Strategic objective cards:")
        for i in range(len(assetLst[e][0]["Strategic objectives"])):
            asset = assetLst[e][0]["Strategic objectives"][i]
            sto_asset = Label(myWin, text=asset)
        frame_lst.append(e)#??

    name_label.pack()
    vp_label.pack()
    lr_label.pack()
    lr_asset.pack()
    so_label.pack()
    so_asset.pack()
    co_label.pack()
    co_asset.pack()
    sto_label.pack()
    sto_asset.pack()
    print(frame_lst)



myWin = Tk()
myWin.title("SWACG")
myWin.iconbitmap("Art/icon.ico")#check me
myWin.geometry("1500x300")

testPlayer=8
testRegion=3
plst=SWACG.assetCreator(testRegion,testPlayer)
flst=SWACG.mapPosition(plst,testPlayer)
img_lst=[]
assetLst = [({'name': 'Ringo Vinda', 'vp': 2, 'location rewards': [{'Fleet Support': '10/5'}],
              'Standard Objectives cards': ['Superior Positions', 'Superior Positions'], 'Campaign Objectives': [],
              'Strategic objectives': ['Ally', 'Repair yards']}, [180, 168]),
            ({'name': 'Ando', 'vp': 2, 'location rewards': [{'Fleet Support': '24/12'}, {'Ordnance': '24/12'}],
              'Standard Objectives cards': [], 'Campaign Objectives': ['Hired Scum'], 'Strategic objectives': []},
             [229, 200]),
            ({'name': 'Cyphar', 'vp': 0, 'location rewards': [{'Squadron': '8/4'}, {'Offensive Retrofit': '8/4'}],
              'Standard Objectives cards': ['Superior Positions'], 'Campaign Objectives': ['Double Agents'],
              'Strategic objectives': ['Resources', 'Ally']}, [249, 249]),
            ({'name': 'Aleen Minor', 'vp': 2, 'location rewards': [{'Squadron': '10/5'}],
              'Standard Objectives cards': ['Marked for Destruction'],
              'Campaign Objectives': ['Prototype Recovery', 'Prototype Recovery'], 'Strategic objectives': []},
             [146, 120]),
            ({'name': 'Bardelberan 7', 'vp': 0,
              'location rewards': [{'Fleet Support': '30/15'}, {'Turbolasers': '30/15'}],
              'Standard Objectives cards': [], 'Campaign Objectives': ['Hired Scum', 'Steel Supplies'],
              'Strategic objectives': ['Repair yards', 'Ally']}, [281, 169])]





card_data(assetLst)

myWin.mainloop()
