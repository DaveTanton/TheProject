import SWACG
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image,ImageGrab

def on_tab_selected(event):
    selected_tab = event.widget.select()

def donothing():
   filewin = Toplevel(myWin)
   button = Button(filewin, text="Do nothing button")
   button.pack()

class SWACG_alpha:
    def __init__(self):
       # self.Campagin_name="TODO"
        self.players = 0
        self.planets = 0
        self.region = 0
        self.regionNum = 0
        self.plst = None
        self.llst = None
        self.img_lst = []

    def generate(self):
       self.players = r.get()
       self.planets = SWACG.num_planets(self.players)
       self.regionNum = 0
       self.region = myCombo.get()
       if self.region == "Core Worlds":
           self.regionNum = 1
       if self.region == "inner Rim":
           self.regionNum= 2
       if self.region == "Mid Rim":
           self.regionNum= 3
       if self.region == "Outer Territories":
           self.regionNum = 4
       self.plst = SWACG.assetCreator (self.regionNum,self.planets)
       self.llst = SWACG.mapPosition (self.plst,self.planets)
       self.icons()
      # self.card_data()
       #print(self.llst)

    def icons(self):
       self.img_lst = []
       self.icon_lst=[]
       self.clear()
       lstObj = SWACG.fileLoader("locRe.txt")
       for i in range(len(self.llst)):
           PPP = ImageTk.PhotoImage(file="art/icons/PPP" + str(SWACG.randomRoll(1, 1)) + ".png")
           cv.create_image((self.llst[i][1][0]), (self.llst[i][1][1]), image=PPP)
           cv.create_text((self.llst[i][1][0]), (self.llst[i][1][1]) + 30, text=self.llst[i][0]["name"], fill="white",tag="nil")
           cv.create_text((self.llst[i][1][0]) - 20, (self.llst[i][1][1]) - 20, text="vp " + str(self.llst[i][0]["vp"]),fill="white",tag="nil")
           for j in range(len(self.llst[i][0]["location rewards"])):
               for k in self.llst[i][0]["location rewards"][j]:
                   if k in lstObj :
                       if j == 0:
                           icon=ImageTk.PhotoImage(file="art/icons/" + self.namereplacer(k) + ".png")
                           cv.create_image((self.llst[i][1][0])+30 , (self.llst[i][1][1])-20 , image=icon, tag="nil")
                       if j == 1:
                           icon = ImageTk.PhotoImage(file="art/icons/" + self.namereplacer(k) + ".png")
                           cv.create_image((self.llst[i][1][0]) + 30, (self.llst[i][1][1]), image=icon, tag="nil")
               self.icon_lst.append(icon)
           self.img_lst.append(PPP)

    def clear(self):
       self.img_lst=[]
       cv.delete("nil")

    def coOrd_regen(self):
        self.llst = SWACG.mapPosition(self.plst, self.planets)
        self.icons()

    def namereplacer(self,name):
        result =  name.replace(" ", "")
        return result

    def card_data(self):
        #card_frame
        #frame_lst
        for e in range(len(self.plst)):
            dynamic_frames = []
            for e in range(len(self.plst)):
                card_frame = LabelFrame(tab2, text="planet card")
                name_label = Label(tab2, text="planet name: " + self.plst[e][0]["name"])
                vp_label = Label(tab2, text="VP:" + str(self.plst[e][0]["vp"]))
                lr_label = Label(tab2, text="Location rewards:")
                for i in range(len(self.plst[e][0]["location rewards"])):
                    for k, v in self.plst[e][0]["location rewards"][i].items():
                        asset = k, v
                        lr_asset = Label(tab2, text=asset)
                so_label = Label(tab2, text="Standard Objective cards:")
                for i in range(len(self.plst[e][0]["Standard Objectives cards"])):
                    asset = self.plst[e][0]["Standard Objectives cards"][i]
                    so_asset = Label(tab2, text=asset)
                co_label = Label(tab2, text="Campaign Objectives cards:")
                for i in range(len(self.plst[e][0]["Campaign Objectives"])):
                    asset = self.plst[e][0]["Campaign Objectives"][i]
                    co_asset = Label(tab2, text=asset)
                sto_label = Label(tab2, text="Strategic objective cards:")
                for i in range(len(self.plst[e][0]["Strategic objectives"])):
                    asset = self.plst[e][0]["Strategic objectives"][i]
                    sto_asset = Label(tab2, text=asset)
                dynamic_frames.append(card_frame)
            card_frame.pack()
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

myWin = Tk()
myWin.title("SWACG")
myWin.iconbitmap("art/icon.ico")# TODO
myWin.geometry("1500x830")


SWACG_assets=SWACG_alpha()

#TODO ADD Menu
#TODO ADD Tabs
#TODO ADD Map selection

mainframe=Frame(myWin)

#menu bar
menubar = Menu(myWin)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=myWin.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

myWin.config(menu=menubar)


tab_parent = ttk.Notebook(mainframe)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="Map Generation")
tab_parent.add(tab2, text="Map Cards")
tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)

menuframe = Frame(mainframe)
t1 = LabelFrame (menuframe,text="Frame One",height=250,width=380)

#enterybox
lbl_snl = Label(t1,text="Sector   ")
snb = Entry(t1)

lbl_snl.grid(row=0,column=0,padx=5,pady=5,sticky=E)
snb.grid(row=0,column=2,columnspan=2,padx=5,pady=5,sticky=E)

#radiobuttons
lbl_players = Label(t1,text="players")

r = IntVar(t1,2)
rb1=Radiobutton(t1,text="2",variable=r, value=2)
rb2=Radiobutton(t1,text="4",variable=r, value=4)
rb3=Radiobutton(t1,text="6",variable=r, value=6)
rb4=Radiobutton(t1,text="8",variable=r, value=8)
rb5=Radiobutton(t1,text="10",variable=r, value=18)

lbl_players.grid(row=2,column=0,padx=10,pady=5)
rb1.grid(row=2,column=1,padx=5,pady=5)
rb2.grid(row=2,column=2,padx=5,pady=5)
rb3.grid(row=2,column=3,padx=5,pady=5)
rb4.grid(row=2,column=4,padx=5,pady=5)
rb4.grid(row=2,column=5,padx=5,pady=5)

#combo box
lbl_region_select=Label(t1,text="Region")

options=["Core Worlds", "inner Rim", "Mid Rim", "Outer Territories"]
myCombo = ttk.Combobox(t1,value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>")

lbl_region_select.grid(row=3,column=0,padx=10,pady=5)
myCombo.grid(row=3,column=1,columnspan=4,padx=10,pady=5)

lbl_map_select=Label(t1,text="Sector map")

options=["map 1", "map 2", "map 3", "map 4"]
myMapCombo = ttk.Combobox(t1,value=options)
myMapCombo.current(0)
myMapCombo.bind("<<ComboboxSelected>>")

lbl_map_select.grid(row=4,column=0,padx=10,pady=5)
myMapCombo.grid(row=4,column=1,columnspan=4,padx=10,pady=5)


lbl_fs = Label(t1,text="Fleet Size")
fsb= Entry(t1)

lbl_fs.grid(row=5,column=0,padx=5,pady=5,sticky=E)
fsb.grid(row=5,column=2,columnspan=2,padx=5,pady=5,sticky=E)

#buttons
btn_generate = Button(t1,text="generate",command= lambda: SWACG_assets.generate())
btn_coOrd_only = Button(t1, text="remap",command= lambda: SWACG_assets.coOrd_regen())
btn_clear = Button(t1,text="clear all",command= lambda: SWACG_assets.clear())

btn_generate.grid(row=6,column=0,columnspan=2,padx=10,pady=5)
btn_coOrd_only.grid(row=6,column=4,columnspan=2,padx=10,pady=5)
btn_clear.grid(row=6,column=2,columnspan=2,padx=10,pady=5)

t2 = LabelFrame (menuframe,text="Frame Two",height=250,width=380)
lbl_players=Label(t2,text="Players")
lbl_p=Label(t2,text="")

lbl_p.pack(side=RIGHT)
lbl_players.pack(side=LEFT)

t3 = LabelFrame (menuframe,text="Frame Three",height=250,width=380)

#t4 = LabelFrame (menuframe,text="placeholder",height=200,width=380)



#details
#sector name
#players
#planets
#fleet size
#fleet brakdown

t1.grid(row=0,column=0,padx=20)
t2.grid(row=1,column=0,padx=20)
t3.grid(row=2,column=0,padx=20)
#t4.pack(side=TOP,padx=20,)

frame_tab_1 = Frame(mainframe)

mapframe = Frame(tab1,height=790,width=1120)
cv = Canvas(mapframe,height=790,width=1120,borderwidth=0,highlightthickness=0)
image1 = ImageTk.PhotoImage(file="art/maps/map2.png")
cv.create_image(0,0,image=image1,anchor=NW)
cv.place(x=0,y=0)

frame_tab_2 = Frame(mainframe)


tab_parent.grid(row=0,column=0)
frame_tab_1.grid(row=0,column=0)
frame_tab_2.grid(row=0,column=0)
mapframe.grid(row=0,column=0)
menuframe.grid(row=0,column=1)
mainframe.grid(row=0,column=0)

myWin.mainloop()
