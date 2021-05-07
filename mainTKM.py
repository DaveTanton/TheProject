import SWACG
import math
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageGrab
import csv

# TODO defining an event inside a class
# TODO look into map issues when changing map
# TODO into lr duplicating resources
# TODO icon.ico
global bg_img

def on_tab_selected(event):
    selected_tab = event.widget.select()

def on_map_change(event):
    cv.delete("map")
    bg_img = ImageTk.PhotoImage(file="art/maps/"+map_combo.get()+".png")
    cv.create_image(0, 0, image=bg_img, anchor=NW, tag="map")
    cv.config(image=bg_img)# causes a traceback error but works?
    cv.place(x=0, y=0)

def do_nothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

class SWACG_main:
    def __init__(self):
        self.name = ""
        self.players = 0
        self.planets = 0
        self.region = 0
        self.region_num = 0
        self.fleet = 0
        self.p_lst = None
        self.l_lst = None
        self.img_lst = []

    def generate(self):
        self.name = snb.get()
        self.players = r.get()
        self.planets = self.num_of_planets(self.players)
        self.region_num = 0
        self.region = region_combo.get()
        if self.region == "Core Worlds":
           self.region_num = 1
        if self.region == "inner Rim":
           self.region_num = 2
        if self.region == "Mid Rim":
           self.region_num = 3
        if self.region == "Outer Territories":
           self.region_num = 4
        self.fleet = int(fsb.get())
        if self.fleet <= 0:
            self.fleet = 200
        self.p_lst = SWACG.asset_creator(self.region_num, self.planets)
        self.l_lst = SWACG.map_position(self.p_lst, self.planets)
        self.icons()
        self.campaign_details()
        self.card_data()

    def icons(self):
       self.img_lst = []
       self.icon_lst = []
       self.clear("nil")
       icon = None
       lst_obj = SWACG.file_loader("locRe.txt")
       for i in range(len(self.l_lst)):
           ppp = ImageTk.PhotoImage(file="art/icons/PPP" + str(SWACG.random_roll(1, 1)) + ".png")
           cv.create_image((self.l_lst[i][1][0]), (self.l_lst[i][1][1]), image=ppp)
           cv.create_text((self.l_lst[i][1][0]), (self.l_lst[i][1][1]) + 30,
                          text=self.l_lst[i][0]["name"], fill="white", tag="nil")
           cv.create_text((self.l_lst[i][1][0]) - 20, (self.l_lst[i][1][1]) - 20,
                          text="vp " + str(self.l_lst[i][0]["vp"]), fill="white", tag="nil")
           for j in range(len(self.l_lst[i][0]["location rewards"])):
               for k in self.l_lst[i][0]["location rewards"][j]:
                   if k in lst_obj:
                       if j == 0:
                           icon = ImageTk.PhotoImage(file="art/icons/" + self.name_replacer(k) + ".png")
                           cv.create_image((self.l_lst[i][1][0])+30, (self.l_lst[i][1][1])-20, image=icon, tag="nil")
                       if j == 1:
                           icon = ImageTk.PhotoImage(file="art/icons/" + self.name_replacer(k) + ".png")
                           cv.create_image((self.l_lst[i][1][0]) + 30, (self.l_lst[i][1][1]), image=icon, tag="nil")
               self.icon_lst.append(icon)
           self.img_lst.append(ppp)

    def campaign_details(self):
        lbl_name_val.config(text=self.name)
        lbl_players_val.config(text=self.players)
        lbl_planets_val.config(text=self.planets)
        lbl_region_val.config(text=self.region)
        self.fleet_breakdown(self.fleet)

    def fleet_breakdown(self, fleet):
        self.fighter = math.ceil(fleet / 3)
        self.ship = fleet - self.fighter
        lbl_fleet_val.config(text=fleet)
        lbl_fleet_ships_val.config(text=str(self.ship))
        lbl_fleet_fighters_val.config(text=str(self.fighter))

    def clear(self, tag):
       self.img_lst = []
       cv.delete(tag)
       self.clear_frame()
       lbl_name_val.config(text=" ")
       lbl_players_val.config(text="0")
       lbl_planets_val.config(text="0")
       lbl_region_val.config(text="0")
       lbl_fleet_val.config(text="0")
       lbl_fleet_ships_val.config(text="0")
       lbl_fleet_fighters_val.config(text="0")

    def num_of_planets(self, players):
        planets = int(math.ceil(players * 3.75) + 1)
        return planets

    def coord_regen(self):
        self.l_lst = SWACG.map_position(self.p_lst, self.planets)
        self.icons()

    def name_replacer(self, name):
        result = name.replace(" ", "")
        return result

    def card_data(self):

        dynamic_frames = []

        lbl_lr_val=Label()
        lbl_so_val=Label()
        lbl_co_val=Label()
        lbl_sto_val=Label()

        for e in range(len(self.p_lst)):
            card_frame =LabelFrame(viewport, text="planet Card")
            name_label = Label(card_frame, text="planet name: " + self.p_lst[e]["name"])
            vp_label = Label(card_frame, text="VP:" + str(self.p_lst[e]["vp"]))
            lbl_lr = Label(card_frame, text="Location rewards:")
            for i in range(len(self.p_lst[e]["location rewards"])):
                for k, v in self.p_lst[e]["location rewards"][i].items():
                    asset = k, v
                    lbl_lr_val=Label(card_frame, text=asset)
            lbl_so=Label(card_frame,text="Standard Objective cards:")
            for i in range(len(self.p_lst[e]["Standard Objectives"])):
                asset = self.p_lst[e]["Standard Objectives"][i]
                lbl_so_val=Label(card_frame,text=asset)
            lbl_co=Label(card_frame,text="Campaign Objectives cards:")
            for i in range(len(self.p_lst[e]["Campaign Objectives"])):
                asset = self.p_lst[e]["Campaign Objectives"][i]
                lbl_co_val=Label(card_frame,text=asset)
            lbl_sto=Label(card_frame,text="Strategic Objectives cards:")
            for i in range(len(self.p_lst[e]["Strategic Objectives"])):
                asset = self.p_lst[e]["Strategic Objectives"][i]
                lbl_sto_val=Label(card_frame,text=asset)
            dynamic_frames.append(card_frame)

            card_frame.pack(side=RIGHT,fill=None, expand=False,padx=5)
            name_label.grid(column=0, row=1)
            vp_label.grid(column=0, row=2)
            lbl_lr.grid(column=0, row=3)
            lbl_lr_val.grid(column=0, row=4)
            lbl_so.grid(column=0, row=5)
            lbl_so_val.grid(column=0, row=6)
            lbl_co.grid(column=0, row=7)
            lbl_co_val.grid(column=0, row=8)
            lbl_sto.grid(column=0, row=9)
            lbl_sto_val.grid(column=0, row=10)

    def save_file(self):
        formats = [("Comma Separated values", "*.csv"), ("Plain Text", "*.txt")]
        file_name = filedialog.asksaveasfilename(parent=root, filetypes=formats, defaultextension="*.*")
        if file_name:
            with open(file_name, 'w') as fp:
                asset_writer = csv.writer(fp)
                asset_writer.writerow(["sector name :", self.name])
                asset_writer.writerow(("number of players :", self.players))
                asset_writer.writerow(["Region :", self.region])
                asset_writer.writerow(["number of planets :", self.planets])
                asset_writer.writerow(["Fleet Size :", self.fleet])
                # write row of header names
                for item in self.p_lst:
                    asset_writer.writerow([item])

    def clear_frame(self):
        for widgets in viewport.winfo_children():
            widgets.destroy()

root = Tk()
root.title("SWACG")
root.iconbitmap("art/icon.ico")
root.geometry("1500x830")

SWACG_assets = SWACG_main()

main_frame = Frame(root)

# menu bar
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=do_nothing)
file_menu.add_command(label="Save Data", command=lambda: SWACG_assets.save_file())
file_menu.add_command(label="Save Map", command=do_nothing)

file_menu.add_separator()

file_menu.add_command(label="About...", command=do_nothing)
file_menu.add_command(label="Help Index", command=do_nothing)

file_menu.add_separator()

file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Tab setup
tab_parent = ttk.Notebook(main_frame)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="Map Generation")
tab_parent.add(tab2, text="Map Cards")
tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)

menu_frame = Frame(main_frame)
t1 = LabelFrame(menu_frame, text="Frame One", height=250, width=380)

# entry box
lbl_snl = Label(t1, text="Sector")
snb = Entry(t1)

lbl_snl.grid(row=0, column=0, padx=5, pady=5, sticky=E)
snb.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky=E)

# radio buttons
lbl_players = Label(t1, text="players")

r = IntVar(t1, 2)
rb1 = Radiobutton(t1, text="2", variable=r, value=2)
rb2 = Radiobutton(t1, text="4", variable=r, value=4)
rb3 = Radiobutton(t1, text="6", variable=r, value=6)
rb4 = Radiobutton(t1, text="8", variable=r, value=8)

lbl_players.grid(row=2, column=0, padx=10, pady=5)
rb1.grid(row=2, column=1, padx=5, pady=5)
rb2.grid(row=2, column=2, padx=5, pady=5)
rb3.grid(row=2, column=3, padx=5, pady=5)
rb4.grid(row=2, column=4, padx=5, pady=5)

# combo box
lbl_region_select = Label(t1, text="Region")

options = ["Core Worlds", "inner Rim", "Mid Rim", "Outer Territories"]
region_combo = ttk.Combobox(t1, value=options)
region_combo.current(0)
region_combo.bind("<<ComboboxSelected>>")

lbl_region_select.grid(row=3, column=0, padx=10, pady=5)
region_combo.grid(row=3, column=1, columnspan=4, padx=10, pady=5)

lbl_map_select = Label(t1, text="Sector map")

options = ["map1", "map2"]
map_combo = ttk.Combobox(t1, value=options)
map_combo.current(0)
map_combo.bind("<<ComboboxSelected>>", on_map_change)

lbl_map_select.grid(row=4, column=0, padx=10, pady=5)
map_combo.grid(row=4, column=1, columnspan=4, padx=10, pady=5)

lbl_fs = Label(t1, text="Fleet Size")
fsb = Entry(t1)
fsb.insert(0, 0)

lbl_fs.grid(row=5, column=0, padx=5, pady=5, sticky=E)
fsb.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky=E)

# buttons
btn_generate = Button(t1, text="generate", command=lambda: SWACG_assets.generate())
btn_coOrd_only = Button(t1, text="remap", command=lambda: SWACG_assets.coord_regen())
btn_clear = Button(t1, text="clear all", command=lambda: SWACG_assets.clear("nil"))

btn_generate.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
btn_coOrd_only.grid(row=6, column=4, columnspan=2, padx=10, pady=5)
btn_clear.grid(row=6, column=2, columnspan=2, padx=10, pady=5)

t2 = LabelFrame(menu_frame, text="Frame Two", height=250, width=380)

lbl_name = Label(t2, text="Sector Name")
lbl_players = Label(t2, text="Players")
lbl_planets = Label(t2, text="Planets in Sector")
lbl_region = Label(t2, text="Region of Sector")
lbl_fleet = Label(t2, text="Fleet size")
lbl_fleet_ships = Label(t2, text="to be spent on ships")
lbl_fleet_fighters = Label(t2, text="to be spent on fighters")

lbl_name_val = Label(t2, text=" ")
lbl_players_val = Label(t2, text="0")
lbl_planets_val = Label(t2, text="0")
lbl_region_val = Label(t2, text="0")
lbl_fleet_val = Label(t2, text="0")
lbl_fleet_ships_val = Label(t2, text="0")
lbl_fleet_fighters_val = Label(t2, text="0")

lbl_name.grid(row=0, column=0)
lbl_players.grid(row=1, column=0)
lbl_planets.grid(row=2, column=0)
lbl_region.grid(row=3, column=0)
lbl_fleet.grid(row=4, column=0)
lbl_fleet_ships.grid(row=5, column=0)
lbl_fleet_fighters.grid(row=6, column=0)

lbl_name_val.grid(row=0, column=1)
lbl_players_val.grid(row=1, column=1)
lbl_planets_val.grid(row=2, column=1)
lbl_region_val.grid(row=3, column=1)
lbl_fleet_val.grid(row=4, column=1)
lbl_fleet_ships_val.grid(row=5, column=1)
lbl_fleet_fighters_val.grid(row=6, column=1)

t3 = LabelFrame(menu_frame, text="Frame Three", height=250, width=380)
# t4 = LabelFrame (menu_frame,text="placeholder",height=200,width=380)

t1.grid(row=0, column=0, padx=20)
t2.grid(row=1, column=0, padx=20)
t3.grid(row=2, column=0, padx=20)
# t4.pack(side=TOP, padx=20)

frame_tab_1 = Frame(main_frame)

map_frame = Frame(tab1, height=790, width=1120)
cv = Canvas(map_frame, height=790, width=1120, borderwidth=0, highlightthickness=0)
bg_img = ImageTk.PhotoImage(file="art/maps/map1.png")
cv.create_image(0, 0, image=bg_img, anchor=NW, tag="map")
cv.place(x=0, y=0)

frame_tab_2 = Frame(main_frame)
scrollFrame = Frame(tab2)
scrollFrame.pack(fill=BOTH, expand=1)

scroll_canvas = Canvas(scrollFrame)
scroll_canvas.pack(side=LEFT, fill=BOTH, expand=True)

scroll_bar = ttk.Scrollbar(scrollFrame, orient=VERTICAL, command=scroll_canvas.yview)
scroll_bar.pack(side=RIGHT, fill=Y)

scroll_canvas.configure(yscrollcommand=scroll_bar.set)
scroll_canvas.bind("<Configure>",
                                lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))
viewport = Frame(scroll_canvas)
scroll_canvas.create_window((0, 0), window=viewport, anchor=NW)

tab_parent.grid(row=0, column=0)
frame_tab_1.grid(row=0, column=0)
frame_tab_2.grid(row=0, column=0)
map_frame.grid(row=0, column=0)
menu_frame.grid(row=0, column=1)
main_frame.grid(row=0, column=0)

root.mainloop()
