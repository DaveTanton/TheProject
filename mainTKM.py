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
# TODO 8.7, 8.6 7.6
#todo dtat validation fleet
#todo scroll missing in some instances (back to a function?)

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

    # "style sheets"

    w_val_s = 5
    w_val_m = 25
    w_val_sm = 10

    ap_e = E
    ap_w = W
    ap=c = CENTER

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
        """
        function gathers user input and generates the play assets into 2 lists
        p_lst (planet list) is the name, vp and details of the asset
        l_lst(location list) is the x,y co ord amended onto the p_lst
        the lists are seperate to make modifing them later eaiser

        clear_viewport() clears all data in the Viewport frame during each clik of the generate button
        icons() generates the play icons based on the p_lst
        campaign_details() justs outputs the details into the UI
        card_Data() outputs the planet data into TAB 2
        """
        self.clear_viewport()
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
        #self.scroll_area()
        self.card_data()

    def icons(self):
        """
        Generates icons based on planet details and map positions based on l_lst out puts to the IMG_lst which is needed
        to out put onto the cv frame

        clear_icon() clears all icons from the viewport when the generate button is clicked
        """

        self.img_lst = []
        self.icon_lst = []
        self.clear_icon("nil")
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
        """
        outputs details to the UI
        """
        lbl_name_val.config(text=self.name)
        lbl_players_val.config(text=self.players)
        lbl_planets_val.config(text=self.planets)
        lbl_region_val.config(text=self.region)
        self.fleet_breakdown(self.fleet)

    def fleet_breakdown(self, fleet):
        """
        :param fleet: takes a INT value as fleet
        :return: returns a breakdown for a campaign legal fleet based on the int in fleet variable
        """
        self.fighter = math.ceil(fleet / 3)
        self.ship = fleet - self.fighter
        lbl_fleet_val.config(text=fleet)
        lbl_fleet_ships_val.config(text=str(self.ship))
        lbl_fleet_fighters_val.config(text=str(self.fighter))

    def clear_icon(self,tag):
        """
        :param tag: takes a string variable that matches the tag attribute
        :return: clears the values based on the tag varible
        """
        self.img_lst = []
        cv.delete(tag)

    def clear(self, tag):
        """
        :param tag: String varible from the tag attribute
        :return: clears all data based on the tag and "zeros" all data
        """
        self.img_lst = []
        cv.delete(tag)
        self.clear_viewport()
        lbl_name_val.config(text=" ")
        lbl_players_val.config(text="0")
        lbl_planets_val.config(text="0")
        lbl_region_val.config(text="0")
        lbl_fleet_val.config(text="0")
        lbl_fleet_ships_val.config(text="0")
        lbl_fleet_fighters_val.config(text="0")

    def clear_viewport(self):
        """
        :return: clears all data in a frame
        """
        for widgets in viewport.winfo_children():
           widgets.destroy()


    def num_of_planets(self, players):
        """
        :param players: a int value 2,4,6,8 number of players
        :return: generates the number of planets to create for the campaign
        """
        planets = int(math.ceil(players * 3.75) + 1)
        return planets

    def coord_regen(self):
        """
        :return: resets the location values in l_lst and reassigns
        """
        self.l_lst = SWACG.map_position(self.p_lst, self.planets)
        self.icons()

    def name_replacer(self, name):
        result = name.replace(" ", "")
        return result

    def card_data(self):
        """
        :return: creates a frame per p_lst item and outputs the results to viewport in TAB2 in the UI
        """
        self.dynamic_frames =[]
        lbl_lr_val = Label()
        lbl_so_val = Label()
        lbl_co_val = Label()
        lbl_sto_val = Label()

        for e in range(len(self.p_lst)):
            card_frame = LabelFrame(viewport, text="planet Card")
            name_label = Label(card_frame, text=self.p_lst[e]["name"],width=self.w_val_sm,anchor=self.ap_w)
            vp_label = Label(card_frame, text="VP: " + str(self.p_lst[e]["vp"]),width=self.w_val_s)

            lbl_lr = Label(card_frame, text="Location rewards:",width=self.w_val_m,anchor=self.ap_w)
            for i in range(len(self.p_lst[e]["location rewards"])):
                for k, v in self.p_lst[e]["location rewards"][i].items():
                    asset = k, v
                    lbl_lr_val = Label(card_frame, text=asset,width=self.w_val_m,anchor=self.ap_w)
                    lbl_lr_val.grid(column=3, row=i+1)

            lbl_so = Label(card_frame, text="Standard Objective cards:",width=self.w_val_m,anchor=self.ap_w)
            for i in range(len(self.p_lst[e]["Standard Objectives"])):
                asset = self.p_lst[e]["Standard Objectives"][i]
                lbl_so_val = Label(card_frame, text=asset,width=self.w_val_m,anchor=self.ap_w)
                lbl_so_val.grid(column=4, row=i+1)

            lbl_co = Label(card_frame, text="Campaign Objectives cards:",width=self.w_val_m,anchor=self.ap_w)
            for i in range(len(self.p_lst[e]["Campaign Objectives"])):
                asset = self.p_lst[e]["Campaign Objectives"][i]
                lbl_co_val = Label(card_frame, text=asset,width=self.w_val_m,anchor=self.ap_w)
                lbl_co_val.grid(column=5, row=i+1)
            # if statement here is a hack to gain a fixed height in each frame
            lbl_sto = Label(card_frame, text="Strategic Objectives cards:",width=self.w_val_m,anchor=self.ap_w)
            if len(self.p_lst[e]["Strategic Objectives"]) >1:
                for i in range(len(self.p_lst[e]["Strategic Objectives"])):
                    asset = self.p_lst[e]["Strategic Objectives"][i]
                    lbl_sto_val = Label(card_frame, text=asset,width=self.w_val_m,anchor=self.ap_w)
                    lbl_sto_val.grid(column=6, row=i+1)
            else:
                for i in range (2):
                    asset = ""
                    lbl_sto_val = Label(card_frame, text=asset,width=self.w_val_m,anchor=self.ap_w)
                    lbl_sto_val.grid(column=6, row=i + 1)

            self.dynamic_frames.append(card_frame)

            card_frame.pack(side=TOP, fill=BOTH, expand=True,)
            name_label.grid(column=1, row=0)
            vp_label.grid(column=2, row=0)

            lbl_lr.grid(column=3, row=0)
            lbl_so.grid(column=4, row=0)
            lbl_co.grid(column=5, row=0)
            lbl_sto.grid(column=6, row=0)

    def save_file(self):
        """
        :return:Menu save file foe CSV and text data
        """
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
"""
    def scroll_area(self):
        # scrollable area (vertical)
        scrollFrame = Frame(tab2)
        scrollFrame.pack(fill=BOTH, expand=1)

        scroll_canvas = Canvas(scrollFrame)
        scroll_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scroll_bar = ttk.Scrollbar(scrollFrame, orient=VERTICAL, command=scroll_canvas.yview)
        
        scroll_bar.pack(side=RIGHT, fill=Y)

        scroll_canvas.configure(yscrollcommand=scroll_bar.set, width=1200)
        scroll_canvas.bind("<Configure>",
                           lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))
        # viewport frame
        self.viewport = Frame(scroll_canvas, width=1200)
        scroll_canvas.create_window((0, 0), window=self.viewport, anchor=NW)
"""
root = Tk()
root.title("SWACG")
root.iconbitmap("art/icon.ico")
root.geometry("1580x840")

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
#/menu bar

# Tab setup
tab_parent = ttk.Notebook(main_frame)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="Map Generation")
tab_parent.add(tab2, text="Map Cards")
tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)
#/tab setup

#main UI start
menu_frame = Frame(main_frame)

# user input area
t1 = LabelFrame(menu_frame, text="Frame Three", height=250, width=280)

# sector box
lbl_snl = Label(t1, text="Sector  ",width=10, anchor=E)
snb = Entry(t1,width=24)

lbl_snl.grid(row=0, column=0, padx=5, pady=5, sticky=E)
snb.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky=E)

# number of players
lbl_players = Label(t1, text="players",width=10, anchor=E)

r = IntVar(t1, 2)
rb1 = Radiobutton(t1, text="2", variable=r, value=2,anchor=CENTER)
rb2 = Radiobutton(t1, text="4", variable=r, value=4,anchor=CENTER)
rb3 = Radiobutton(t1, text="6", variable=r, value=6,anchor=CENTER)
rb4 = Radiobutton(t1, text="8", variable=r, value=8,anchor=CENTER)

lbl_players.grid(row=2, column=0, padx=10, pady=5)
rb1.grid(row=2, column=1, padx=1, pady=1)
rb2.grid(row=2, column=2, padx=1, pady=1)
rb3.grid(row=2, column=3, padx=1, pady=1)
rb4.grid(row=2, column=4, padx=1, pady=1)

# region location
lbl_region_select = Label(t1, text="Region",width=10, anchor=E)

options = ["Core Worlds", "inner Rim", "Mid Rim", "Outer Territories"]
region_combo = ttk.Combobox(t1, value=options)
region_combo.current(0)
region_combo.bind("<<ComboboxSelected>>")

lbl_region_select.grid(row=3, column=0, padx=10, pady=5)
region_combo.grid(row=3, column=1, columnspan=4, padx=10, pady=5)

lbl_map_select = Label(t1, text="Sector map",width=10, anchor=E)

# map selection
options = ["map1", "map2"]
map_combo = ttk.Combobox(t1, value=options)
map_combo.current(0)
map_combo.bind("<<ComboboxSelected>>", on_map_change)

lbl_map_select.grid(row=4, column=0, padx=10, pady=5)
map_combo.grid(row=4, column=1, columnspan=4, padx=10, pady=5)

# fleet size
lbl_fs = Label(t1, text="Fleet Size",width=10, anchor=E)
fsb = Entry(t1,width=24)
fsb.insert(0, 0)

lbl_fs.grid(row=5, column=0, padx=5, pady=5)
fsb.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# User input area buttions

#/user input area

# campaign data display
t2 = LabelFrame(menu_frame, text="Frame Three", height=250, width=280)

lbl_name = Label(t2, text="Sector Name",width=25,anchor=E)
lbl_players = Label(t2, text="Players",width=25,anchor=E)
lbl_planets = Label(t2, text="Planets in Sector",width=25,anchor=E)
lbl_region = Label(t2, text="Region of Sector",width=25,anchor=E)
lbl_fleet = Label(t2, text="Fleet size",width=25,anchor=E)
lbl_fleet_ships = Label(t2, text="to be spent on ships",width=25,anchor=E)
lbl_fleet_fighters = Label(t2, text="to be spent on fighters",width=25,anchor=E)

lbl_name_val = Label(t2, text=" ",width=20,anchor=W)
lbl_players_val = Label(t2, text="0",width=20,anchor=W)
lbl_planets_val = Label(t2, text="0",width=20,anchor=W)
lbl_region_val = Label(t2, text="0",width=20,anchor=W)
lbl_fleet_val = Label(t2, text="0",width=20,anchor=W)
lbl_fleet_ships_val = Label(t2, text="0",width=20,anchor=W)
lbl_fleet_fighters_val = Label(t2, text="0",width=20,anchor=W)

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

#/user data display

#map key area
t3 = LabelFrame(menu_frame, text="Frame Three", height=250, width=280)

#/map key area
t4 = LabelFrame(menu_frame)
t4_center_frame = Frame(t4)
btn_generate = Button(t4_center_frame, text="generate", command=lambda: SWACG_assets.generate(),width=10)
btn_coOrd_only = Button(t4_center_frame, text="remap", command=lambda: SWACG_assets.coord_regen(),width=10)
btn_clear = Button(t4_center_frame, text="clear all", command=lambda: SWACG_assets.clear("nil"),width=10)

btn_generate.pack(side=LEFT)
btn_coOrd_only.pack(side=LEFT)
btn_clear.pack(side=LEFT)
t4_center_frame.pack()
t1.pack(side=TOP,fill=BOTH,expand=True)
t2.pack(side=TOP,fill=BOTH,expand=True)
t3.pack(side=TOP,fill=BOTH,expand=True)
t4.pack(side=TOP,fill=BOTH,expand=True)

#TAB 1 START
frame_tab_1 = Frame(main_frame)

#map display
map_frame = Frame(tab1, height=800, width=1200)
cv = Canvas(map_frame, height=800, width=1200, borderwidth=0, highlightthickness=0)
bg_img = ImageTk.PhotoImage(file="art/maps/map1.png")
cv.create_image(0, 0, image=bg_img, anchor=NW, tag="map")
cv.place(x=0, y=0)
#/map display
#/TAB1 END

#TAB2 START
frame_tab_2 = Frame(main_frame)

scrollFrame = Frame(tab2)
scrollFrame.pack(fill=BOTH, expand=1)

scroll_canvas = Canvas(scrollFrame)
scroll_canvas.pack(side=LEFT, fill=BOTH, expand=True)

scroll_bar = ttk.Scrollbar(scrollFrame, orient=VERTICAL, command=scroll_canvas.yview)
scroll_bar.pack(side=RIGHT, fill=Y)

scroll_canvas.configure(yscrollcommand=scroll_bar.set, width=1200)
scroll_canvas.bind("<Configure>",
                   lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))
# viewport frame
viewport = Frame(scroll_canvas, width=1200)
scroll_canvas.create_window((0, 0), window=viewport, anchor=NW)

#/viewport frame
#/TAB2 END

tab_parent.grid(row=0, column=0)
frame_tab_1.grid(row=0, column=0)
frame_tab_2.grid(row=0, column=0)
map_frame.grid(row=0, column=0)
menu_frame.grid(row=0, column=1)
main_frame.grid(row=0, column=0)

root.mainloop()
#main UI end
