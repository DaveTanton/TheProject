import SWACG
import SWACG_stylesheet
import math
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from ttkthemes import ThemedTk, THEMES

from PIL import ImageTk, Image, ImageGrab
import csv


# TODO defining an event inside a class
# TODO look into map issues when changing map
# TODO icon.ico

global bg_img

def on_tab_selected(event):
    selected_tab = event.widget.select()

def on_map_change(event):
    map_canvas.delete("map")
    bg_img = ImageTk.PhotoImage(file="art/maps/"+wid_map_combo.get()+".png")
    map_canvas.create_image(0, 0, image=bg_img, anchor="nw", tag="map")
    map_canvas.config(image=bg_img)  # causes a traceback error but works?
    map_canvas.place(x=0, y=0)

class SWACG_main:

    # "style sheets"

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
        self.clear_frame(tab2)
        self.name = snb.get()
        self.players = r.get()
        self.planets = self.num_of_planets(self.players)
        self.region_num = 0
        self.region = wid_region_combo.get()
        if self.region == "Core Worlds and Colonies":
           self.region_num = 1
        if self.region == "inner Rim and Expansion Region":
           self.region_num = 2
        if self.region == "Mid Rim":
           self.region_num = 3
        if self.region == "Outer Rim Territories":
           self.region_num = 4
        self.fleet = int(fs_val.get())
        if self.fleet <= 0:
            self.fleet = 200
        self.p_lst = SWACG.asset_creator(self.region_num, self.planets)
        self.l_lst = SWACG.map_position(self.p_lst, self.planets)
        self.icons()
        self.campaign_details()
        self.scroll()

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
           ppp = ImageTk.PhotoImage(file="art/icons/PPP" + str(SWACG.random_roll(1, 4)) + ".png")
           map_canvas.create_image((self.l_lst[i][1][0]), (self.l_lst[i][1][1]), image=ppp)
           map_canvas.create_text((self.l_lst[i][1][0]), (self.l_lst[i][1][1]) + 30,
                          text=self.l_lst[i][0]["name"], fill="white", tag="nil")
           map_canvas.create_text((self.l_lst[i][1][0]) - 20, (self.l_lst[i][1][1]) - 20,
                          text="vp " + str(self.l_lst[i][0]["vp"]), fill="white", tag="nil")
           for j in range(len(self.l_lst[i][0]["location rewards"])):
               for k in self.l_lst[i][0]["location rewards"][j]:
                   if k in lst_obj:
                       if j == 0:
                           icon = ImageTk.PhotoImage(file="art/icons/" + self.name_replacer(k) + ".png")
                           map_canvas.create_image((self.l_lst[i][1][0])+30, (self.l_lst[i][1][1])-20, image=icon, tag="nil")
                       if j == 1:
                           icon = ImageTk.PhotoImage(file="art/icons/" + self.name_replacer(k) + ".png")
                           map_canvas.create_image((self.l_lst[i][1][0]) + 30, (self.l_lst[i][1][1]), image=icon, tag="nil")
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
        map_canvas.delete(tag)

    def clear(self, tag):
        """
        :param tag: String varible from the tag attribute
        :return: clears all data based on the tag and "zeros" all data
        """
        self.img_lst = []
        map_canvas.delete(tag)
        self.clear_frame(tab2)
        lbl_name_val.config(text=" ")
        lbl_players_val.config(text="0")
        lbl_planets_val.config(text="0")
        lbl_region_val.config(text="0")
        lbl_fleet_val.config(text="0")
        lbl_fleet_ships_val.config(text="0")
        lbl_fleet_fighters_val.config(text="0")

    def clear_frame(self,frame):
        """
        :return: clears all data in a frame
        """
        for widgets in frame.winfo_children():
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

    def p_title(self, u_frame, u_text):
        lbl_title = tk.Label(u_frame, text=u_text,
                             anchor=SWACG_stylesheet.txt_pos_center,
                             bg=SWACG_stylesheet.bg_mid_grey,
                             fg=SWACG_stylesheet.fg_light_grey,
                             font=('verdana', 15, "bold"),
                             pady=SWACG_stylesheet.num_val_25)

        lbl_title.pack(side="top", fill="both", expand=True)

    def card_data(self):
        """
        :return: creates a frame per p_lst item and outputs the results to viewport in TAB2 in the UI
        """
        lbl_lr_val = tk.Label()
        lbl_so_val = tk.Label()
        lbl_co_val = tk.Label()
        lbl_sto_val = tk.Label()

        self.p_title(self.viewport, "Planet List")

        for e in range(len(self.p_lst)):
            card_frame = tk.LabelFrame(self.viewport,
                                       bg=SWACG_stylesheet.bg_dark_grey,
                                       borderwidth=2,
                                       highlightbackground=SWACG_stylesheet.fg_light_grey,
                                       highlightthickness=SWACG_stylesheet.nil_val,
                                       )

            name_label = tk.Label(card_frame, text=self.p_lst[e]["name"],
                                  width=SWACG_stylesheet.num_val_25,
                                  anchor=SWACG_stylesheet.txt_pos_east,
                                  bg=SWACG_stylesheet.bg_dark_grey,
                                  fg=SWACG_stylesheet.fg_light_grey,
                                  padx=SWACG_stylesheet.num_val_25)

            vp_label = tk.Label(card_frame, text="VP: " + str(self.p_lst[e]["vp"]),
                                width=SWACG_stylesheet.num_val_5,
                                anchor=SWACG_stylesheet.txt_pos_west,
                                bg=SWACG_stylesheet.bg_dark_grey,
                                fg=SWACG_stylesheet.fg_light_grey)

            lbl_lr = tk.Label(card_frame, text="Location rewards:",
                              width=SWACG_stylesheet.num_val_25,
                              anchor=SWACG_stylesheet.txt_pos_west,
                              bg=SWACG_stylesheet.bg_dark_grey,
                              fg=SWACG_stylesheet.fg_light_grey)

            for i in range(len(self.p_lst[e]["location rewards"])):
                for k, v in self.p_lst[e]["location rewards"][i].items():
                    asset = k, v
                    lbl_lr_val = tk.Label(card_frame, text=asset,
                                          width=SWACG_stylesheet.num_val_25,
                                          anchor=SWACG_stylesheet.txt_pos_west,
                                          bg=SWACG_stylesheet.bg_dark_grey,
                                          fg=SWACG_stylesheet.fg_light_grey)
                    lbl_lr_val.grid(column=3, row=i+1)

            lbl_so = tk.Label(card_frame, text="Standard Objective cards:",
                              width=SWACG_stylesheet.num_val_25,
                              anchor=SWACG_stylesheet.txt_pos_west,
                              bg=SWACG_stylesheet.bg_dark_grey,
                              fg=SWACG_stylesheet.fg_light_grey)

            for i in range(len(self.p_lst[e]["Standard Objectives"])):
                asset = self.p_lst[e]["Standard Objectives"][i]
                lbl_so_val = tk.Label(card_frame, text=asset,
                                      width=SWACG_stylesheet.num_val_25,
                                      anchor=SWACG_stylesheet.txt_pos_west,
                                      bg=SWACG_stylesheet.bg_dark_grey,
                                      fg=SWACG_stylesheet.fg_light_grey)
                lbl_so_val.grid(column=4, row=i+1)

            lbl_co = tk.Label(card_frame, text="Campaign Objectives cards:",
                              width=SWACG_stylesheet.num_val_25,
                              anchor=SWACG_stylesheet.txt_pos_west,
                              bg=SWACG_stylesheet.bg_dark_grey,
                              fg=SWACG_stylesheet.fg_light_grey)

            for i in range(len(self.p_lst[e]["Campaign Objectives"])):
                asset = self.p_lst[e]["Campaign Objectives"][i]
                lbl_co_val = tk.Label(card_frame, text=asset,
                                      width=SWACG_stylesheet.num_val_25,
                                      anchor=SWACG_stylesheet.txt_pos_west,
                                      bg=SWACG_stylesheet.bg_dark_grey,
                                      fg=SWACG_stylesheet.fg_light_grey)
                lbl_co_val.grid(column=5, row=i+1)
            # if statement here is a hack to gain a fixed height in each frame
            lbl_sto = tk.Label(card_frame, text="Strategic Objectives cards:",
                               width=SWACG_stylesheet.num_val_25,
                               anchor=SWACG_stylesheet.txt_pos_west,
                               bg=SWACG_stylesheet.bg_dark_grey,
                               fg=SWACG_stylesheet.fg_light_grey)

            if len(self.p_lst[e]["Strategic Objectives"]) > 1:
                for i in range(len(self.p_lst[e]["Strategic Objectives"])):
                    asset = self.p_lst[e]["Strategic Objectives"][i]
                    lbl_sto_val = tk.Label(card_frame, text=asset,
                                           width=SWACG_stylesheet.num_val_25,
                                           anchor=SWACG_stylesheet.txt_pos_west,
                                           bg=SWACG_stylesheet.bg_dark_grey,
                                           fg=SWACG_stylesheet.fg_light_grey)
                    lbl_sto_val.grid(column=6, row=i+1)
            else:
                for i in range(2):
                    asset = ""
                    lbl_sto_val = tk.Label(card_frame, text=asset,
                                           width=SWACG_stylesheet.num_val_25,
                                           anchor=SWACG_stylesheet.txt_pos_west,
                                           bg=SWACG_stylesheet.bg_dark_grey,
                                           fg=SWACG_stylesheet.fg_light_grey)
                    lbl_sto_val.grid(column=6, row=i + 1)

            card_frame.pack(side="top", fill="both", expand=True, ipadx=10, ipady=10)

            name_label.grid(column=1, row=0)
            vp_label.grid(column=2, row=0)

            lbl_lr.grid(column=3, row=0)
            lbl_so.grid(column=4, row=0)
            lbl_co.grid(column=5, row=0)
            lbl_sto.grid(column=6, row=0)

    def scroll(self):
        """

        :return:
        """

        scroll_frame = ttk.Frame(tab2)
        scroll_frame.pack(fill="both", expand=1)

        scroll_canvas = tk.Canvas(scroll_frame, borderwidth=0, highlightthickness=0,background=SWACG_stylesheet.bg_mid_grey)
        scroll_canvas.pack(side="left", fill="both", expand=1)

        scroll_bar = ttk.Scrollbar(scroll_frame, orient="vertical", command=scroll_canvas.yview)
        scroll_bar.pack(side="right", fill="y")

        scroll_canvas.configure(yscrollcommand=scroll_bar.set, width=1150)
        scroll_canvas.bind("<Configure>",
                           lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))
        self.viewport = tk.Frame(scroll_canvas)
        scroll_canvas.create_window((0, 0), window=self.viewport, anchor="nw")
        self.card_data()

    def save_file(self):
        """
        :return:Menu save file fo CSV and text data
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

    def save_img(self):
        formats = [("Portable Network Graphics", "*.PNG")]
        file = filedialog.asksaveasfilename(parent=root, filetypes=formats, defaultextension="*.*")
        x = root.winfo_rootx() + map_canvas.winfo_x()
        y = root.winfo_rooty() + map_canvas.winfo_y()
        x1 = x + map_canvas.winfo_width()
        y1 = y + map_canvas.winfo_height()
        ImageGrab.grab(bbox=(x, y, x1, y1)).save(file)

    def splash_screen(self):
        global splash_img_title

        splash_root = tk.Toplevel(root)
        splash_root.configure(background=SWACG_stylesheet.bg_dark_grey)
        #splash_root.overrideredirect(True)
        splash_root.geometry("500x350")

        splash_img_title = ImageTk.PhotoImage(Image.open("art/SWACG_Title_1.png"))
        lbl_img_title = tk.Label(splash_root,image=splash_img_title,background=SWACG_stylesheet.bg_dark_grey)
        lbl_img_title.pack(pady=20)

        splash_label_by = ttk.Label(splash_root, text="David Tanton",background=SWACG_stylesheet.bg_dark_grey)
        splash_blurb = ttk.Label(splash_root,text="This is not an official endorsed product FFG",
                                 background=SWACG_stylesheet.bg_dark_grey)
        splash_blurb_1 = ttk.Label(splash_root, text="If you have paid for this you've been had",
                                   background=SWACG_stylesheet.bg_dark_grey)
        splash_button = ttk.Button(splash_root, text="close", command=lambda: splash_root.destroy())

        splash_label_by.pack(pady=20, padx=20)
        splash_blurb.pack()
        splash_blurb_1.pack()
        splash_button.pack(ipadx=10, ipady=10, pady=20, padx=20)
        splash_root.mainloop()

root = ThemedTk(theme="black",themebg=True)
""" 
# avaliable themes in the package
['adapta', 'aquativo', 'arc', 'black', 'blue', 'breeze', 'clearlooks', 'elegance', 'equilux', 'itft1', 'keramik', 
'kroc', 'plastik', 'radiance', 'scidblue', 'scidgreen', 'scidgrey', 'scidmint', 'scidpink', 'scidpurple', 'scidsand', 
'smog', 'ubuntu', 'winxpblue', 'yaru']
"""
root.title("SWACG")
root.iconbitmap("art/icon.ico")

# starts app in the middle of the screen
app_width = 1650
app_height = 880

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenmmheight()

x_app_coord = (screen_width/2)-(app_width/2)
y_app_coord = (screen_height/2)-(app_height/2)

# coords have to be an int
root.geometry(f"{app_width}x{app_height}+{int(x_app_coord)}+{int(y_app_coord)}")

SWACG_assets = SWACG_main()

style = ttk.Style()

style.configure("dark.TRadiobutton",background=SWACG_stylesheet.bg_dark_grey)

style.configure("dark.TLabel",background=SWACG_stylesheet.bg_dark_grey)

style.configure("dark.TFrame",
                background=SWACG_stylesheet.bg_dark_grey,
                borderwidth=2,
                highlightbackground=SWACG_stylesheet.fg_light_grey,
                highlightthickness=SWACG_stylesheet.nil_val)

main_frame = ttk.Frame(root)

# menu bar
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save Data", command=lambda: SWACG_assets.save_file())
file_menu.add_command(label="Save Map", command=lambda: SWACG_assets.save_img())

file_menu.add_separator()
file_menu.add_command(label="About...", command=lambda: SWACG_assets.splash_screen())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
# /menu bar

# Tab setup
tab_parent = ttk.Notebook(main_frame)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="Map Generation")
tab_parent.add(tab2, text="Map Cards")
tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)
# /tab setup

# main UI start
menu_frame = ttk.Frame(main_frame)

img_frame = ttk.Frame(menu_frame)
img_title = ImageTk.PhotoImage(Image.open("art/SWACG_Title_1.png"))
lbl_img_title = ttk.Label(img_frame, image=img_title)
lbl_img_title.pack(pady=20)

# user input area
lbl_t1 = ttk.Label(menu_frame, text="Campaign selection", style="dark.TLabel")
t1 = ttk.LabelFrame(menu_frame, labelwidget=lbl_t1, height=250, width=280, style="dark.TFrame")



# sector box
lbl_snl = ttk.Label(t1, text="Sector", style="dark.TLabel")
snb = ttk.Entry(t1)

snb.insert(0, "name")  # inserts a default value

lbl_snl.grid(row=0, column=0, padx=10, sticky=SWACG_stylesheet.ttk_pos_nsew)
snb.grid(row=0, column=1, columnspan=4, padx=10, pady=10, sticky=SWACG_stylesheet.ttk_pos_nsew)

# number of players
lbl_players = ttk.Label(t1, text="players", width=10, style="dark.TLabel")

r = tk.IntVar(t1, 2)

rb1 = ttk.Radiobutton(t1, text="2", variable=r, value=2,style="dark.TRadiobutton")
rb2 = ttk.Radiobutton(t1, text="4", variable=r, value=4,style="dark.TRadiobutton")
rb3 = ttk.Radiobutton(t1, text="6", variable=r, value=6,style="dark.TRadiobutton")
rb4 = ttk.Radiobutton(t1, text="8", variable=r, value=8,style="dark.TRadiobutton")

lbl_players.grid(row=2, column=0, padx=10, pady=10, sticky=SWACG_stylesheet.ttk_pos_nsew)

rb1.grid(row=2, column=1, padx=1, pady=1, sticky=SWACG_stylesheet.ttk_pos_nsew)
rb2.grid(row=2, column=2, padx=1, pady=1, sticky=SWACG_stylesheet.ttk_pos_nsew)
rb3.grid(row=2, column=3, padx=1, pady=1, sticky=SWACG_stylesheet.ttk_pos_nsew)
rb4.grid(row=2, column=4, padx=1, pady=1, sticky=SWACG_stylesheet.ttk_pos_nsew)

# region location
lbl_region_select = ttk.Label(t1, text="Region", width=10, style="dark.TLabel")

options = ["Core Worlds and Colonies", "inner Rim and Expansion Region", "Mid Rim", "Outer Rim Territories"]
wid_region_combo = ttk.Combobox(t1, value=options)
wid_region_combo.current(0)
wid_region_combo.bind("<<ComboboxSelected>>")

lbl_region_select.grid(row=3, column=0, padx=10)
wid_region_combo.grid(row=3, column=1, columnspan=4, padx=10, pady=10, sticky=SWACG_stylesheet.ttk_pos_nsew)

# map selection
lbl_map_select = ttk.Label(t1, text="Sector map", style="dark.TLabel")

options = ["map1", "map2", "map3"]
wid_map_combo = ttk.Combobox(t1, value=options)
wid_map_combo.current(0)
wid_map_combo.bind("<<ComboboxSelected>>", on_map_change)

lbl_map_select.grid(row=4, column=0, padx=10, sticky=SWACG_stylesheet.ttk_pos_nsew)
wid_map_combo.grid(row=4, column=1, columnspan=4, padx=10, pady=10, sticky=SWACG_stylesheet.ttk_pos_nsew)

# combo box style

t1.option_add("*TCombobox*Listbox*Background", SWACG_stylesheet.bg_dark_grey)
t1.option_add("*TCombobox*Listbox*Foreground", SWACG_stylesheet.bg_light_grey)
t1.option_add("*TCombobox*Listbox*selectBackground", SWACG_stylesheet.bg_light_grey)
t1.option_add("*TCombobox*Listbox*selectForeground", SWACG_stylesheet.bg_dark_grey)

# fleet size
lbl_fs = ttk.Label(t1, text="Fleet Size", style="dark.TLabel")
fs_val = ttk.Entry(t1)
fs_val.insert(0, 200)  # inserts a default value

check = root.register(SWACG.callback)  # calls data validation on entery box but only allows numbers
fs_val.config(validate="key", validatecommand=(check, "%P"))

lbl_fs.grid(row=5, column=0, padx=10,sticky=SWACG_stylesheet.ttk_pos_nsew)
fs_val.grid(row=5, column=1, columnspan=4,padx=10, pady=10, sticky=SWACG_stylesheet.ttk_pos_nsew)

# /user input area

# campaign data display
lbl_t2 = ttk.Label(menu_frame, text="Campaign details", style="dark.TLabel")
t2 = ttk.LabelFrame(menu_frame, labelwidget=lbl_t2, height=250, width=280, style="dark.TFrame")

lbl_name = ttk.Label(t2, text="Sector Name", width=SWACG_stylesheet.num_val_25, style="dark.TLabel")
lbl_players = ttk.Label(t2, text="Players", width=SWACG_stylesheet.num_val_25, style="dark.TLabel")
lbl_planets = ttk.Label(t2, text="Planets in Sector", width=SWACG_stylesheet.num_val_25, style="dark.TLabel")
lbl_region = ttk.Label(t2, text="Region of Sector", width=SWACG_stylesheet.num_val_25, style="dark.TLabel")
lbl_fleet = ttk.Label(t2, text="Fleet size", width=SWACG_stylesheet.num_val_25, style="dark.TLabel")
lbl_fleet_ships = ttk.Label(t2, text="to be spent on ships", width=SWACG_stylesheet.num_val_25, style="dark.TLabel")
lbl_fleet_fighters = ttk.Label(t2, text="to be spent on fighters", width=SWACG_stylesheet.num_val_25,
                               style="dark.TLabel")

lbl_name_val = ttk.Label(t2, text=" ", width=SWACG_stylesheet.num_val_20, style="dark.TLabel")
lbl_players_val = ttk.Label(t2, text="0", width=SWACG_stylesheet.num_val_20, style="dark.TLabel")
lbl_planets_val = ttk.Label(t2, text="0", width=SWACG_stylesheet.num_val_20, style="dark.TLabel")
lbl_region_val = ttk.Label(t2, text="0", width=SWACG_stylesheet.num_val_20, style="dark.TLabel")
lbl_fleet_val = ttk.Label(t2, text="0", width=SWACG_stylesheet.num_val_20, style="dark.TLabel")
lbl_fleet_ships_val = ttk.Label(t2, text="0", width=SWACG_stylesheet.num_val_20, style="dark.TLabel")
lbl_fleet_fighters_val = ttk.Label(t2, text="0", width=SWACG_stylesheet.num_val_20, style="dark.TLabel")

lbl_name.grid(row=0, column=0, sticky="nsew", padx=10)
lbl_players.grid(row=1, column=0, sticky="nsew", padx=10)
lbl_planets.grid(row=2, column=0, sticky="nsew", padx=10)
lbl_region.grid(row=3, column=0, sticky="nsew", padx=10)
lbl_fleet.grid(row=4, column=0, sticky="nsew", padx=10)
lbl_fleet_ships.grid(row=5, column=0, sticky="nsew", padx=10)
lbl_fleet_fighters.grid(row=6, column=0, sticky="nsew", padx=10)

lbl_name_val.grid(row=0, column=1, sticky="nsew", padx=10)
lbl_players_val.grid(row=1, column=1, sticky="nsew", padx=10)
lbl_planets_val.grid(row=2, column=1, sticky="nsew", padx=10)
lbl_region_val.grid(row=3, column=1, sticky="nsew", padx=10)
lbl_fleet_val.grid(row=4, column=1, sticky="nsew", padx=10)
lbl_fleet_ships_val.grid(row=5, column=1, sticky="nsew", padx=10)
lbl_fleet_fighters_val.grid(row=6, column=1, sticky="nsew", padx=10)

# /user data display

# map key area
lbl_t3 = ttk.Label(menu_frame, text="Map key", style="dark.TLabel")
t3 = ttk.LabelFrame(menu_frame, labelwidget=lbl_t3, height=250, width=280, style="dark.TFrame")
# fake column 1
lbl_lr_OR = ttk.Label(t3, text="Offensive Retrofit", style="dark.TLabel")
lbl_lr_DR = ttk.Label(t3, text="Defensive Retrofit", style="dark.TLabel")
lbl_lr_ST = ttk.Label(t3, text="Support Team", style="dark.TLabel")
lbl_lr_Of = ttk.Label(t3, text="Officer", style="dark.TLabel")
lbl_lr_Ti = ttk.Label(t3, text="Title", style="dark.TLabel")
lbl_lr_Or = ttk.Label(t3, text="Ordnance", style="dark.TLabel")

img_lr_OR = ImageTk.PhotoImage(Image.open("art/icons/OffensiveRetrofit.png"))
img_lr_DR = ImageTk.PhotoImage(Image.open("art/icons/DefensiveRetrofit.png"))
img_lr_ST = ImageTk.PhotoImage(Image.open("art/icons/SupportTeam.png"))
img_lr_Of = ImageTk.PhotoImage(Image.open("art/icons/Officer.png"))
img_lr_Ti = ImageTk.PhotoImage(Image.open("art/icons/Title.png"))
img_lr_Or = ImageTk.PhotoImage(Image.open("art/icons/Ordnance.png"))

lbl_img_lr_OR = ttk.Label(t3, image=img_lr_OR, style="dark.TLabel")
lbl_img_lr_DR = ttk.Label(t3, image=img_lr_DR, style="dark.TLabel")
lbl_img_lr_ST = ttk.Label(t3, image=img_lr_ST, style="dark.TLabel")
lbl_img_lr_Of = ttk.Label(t3, image=img_lr_Of, style="dark.TLabel")
lbl_img_lr_Ti = ttk.Label(t3, image=img_lr_Ti, style="dark.TLabel")
lbl_img_lr_Or = ttk.Label(t3, image=img_lr_Or, style="dark.TLabel")

lbl_lr_OR.grid(column=0, row=0, sticky="nsew", padx=10)
lbl_lr_DR.grid(column=0, row=1, sticky="nsew", padx=10)
lbl_lr_ST.grid(column=0, row=2, sticky="nsew", padx=10)
lbl_lr_Of.grid(column=0, row=3, sticky="nsew", padx=10)
lbl_lr_Ti.grid(column=0, row=4, sticky="nsew", padx=10)
lbl_lr_Or.grid(column=0, row=5, sticky="nsew", padx=10)

lbl_img_lr_OR.grid(column=1, row=0, sticky="nsew", padx=10)
lbl_img_lr_DR.grid(column=1, row=1, sticky="nsew", padx=10)
lbl_img_lr_ST.grid(column=1, row=2, sticky="nsew", padx=10)
lbl_img_lr_Of.grid(column=1, row=3, sticky="nsew", padx=10)
lbl_img_lr_Ti.grid(column=1, row=4, sticky="nsew", padx=10)
lbl_img_lr_Or.grid(column=1, row=5, sticky="nsew", padx=10)
# /end fake column

# fake column 2
lbl_lr_FC = ttk.Label(t3, text="Fleet Command", style="dark.TLabel")
lbl_lr_IC = ttk.Label(t3, text="Ion Cannons", style="dark.TLabel")
lbl_lr_Tu = ttk.Label(t3, text="Turbolasers", style="dark.TLabel")
lbl_lr_Er = ttk.Label(t3, text="Experimental Retrofit", style="dark.TLabel")
lbl_lr_WT = ttk.Label(t3, text="Weapons Team", style="dark.TLabel")
lbl_lr_FS = ttk.Label(t3, text="Fleet Support", style="dark.TLabel")

img_lr_FC = ImageTk.PhotoImage(Image.open("art/icons/FleetCommand.png"))
img_lr_IC = ImageTk.PhotoImage(Image.open("art/icons/IonCannons.png"))
img_lr_Tu = ImageTk.PhotoImage(Image.open("art/icons/Turbolasers.png"))
img_lr_Er = ImageTk.PhotoImage(Image.open("art/icons/ExperimentalRetrofit.png"))
img_lr_WT = ImageTk.PhotoImage(Image.open("art/icons/WeaponsTeam.png"))
img_lr_FS = ImageTk.PhotoImage(Image.open("art/icons/FleetSupport.png"))

lbl_img_lr_FC = ttk.Label(t3, image=img_lr_OR, style="dark.TLabel")
lbl_img_lr_IC = ttk.Label(t3, image=img_lr_DR, style="dark.TLabel")
lbl_img_lr_Tu = ttk.Label(t3, image=img_lr_ST, style="dark.TLabel")
lbl_img_lr_Er = ttk.Label(t3, image=img_lr_Of, style="dark.TLabel")
lbl_img_lr_WT = ttk.Label(t3, image=img_lr_Ti, style="dark.TLabel")
lbl_img_lr_FS = ttk.Label(t3, image=img_lr_Or, style="dark.TLabel")

lbl_lr_FC.grid(column=2, row=0, sticky="nsew", padx=10)
lbl_lr_IC.grid(column=2, row=1, sticky="nsew", padx=10)
lbl_lr_Tu.grid(column=2, row=2, sticky="nsew", padx=10)
lbl_lr_Er.grid(column=2, row=3, sticky="nsew", padx=10)
lbl_lr_WT.grid(column=2, row=4, sticky="nsew", padx=10)
lbl_lr_FS.grid(column=2, row=5, sticky="nsew", padx=10)

lbl_img_lr_FC.grid(column=4, row=0, sticky="nsew", padx=10)
lbl_img_lr_IC.grid(column=4, row=1, sticky="nsew", padx=10)
lbl_img_lr_Tu.grid(column=4, row=2, sticky="nsew", padx=10)
lbl_img_lr_Er.grid(column=4, row=3, sticky="nsew", padx=10)
lbl_img_lr_WT.grid(column=4, row=4, sticky="nsew", padx=10)
lbl_img_lr_FS.grid(column=4, row=5, sticky="nsew", padx=10)

# /map key area

t4 = ttk.LabelFrame(menu_frame)

t4_center_frame = ttk.Frame(t4, style="SWACG.TFrame")

btn_generate = ttk.Button(t4_center_frame, text="generate", command=lambda: SWACG_assets.generate(), width=15,
                          style="TButton")

btn_coOrd_only = ttk.Button(t4_center_frame, text="remap", command=lambda: SWACG_assets.coord_regen(), width=15)

btn_clear = ttk.Button(t4_center_frame, text="clear all", command=lambda: SWACG_assets.clear("nil"), width=15)

btn_generate.pack(side="left")
btn_coOrd_only.pack(side="left", padx=10)
btn_clear.pack(side="left")
t4_center_frame.pack()
img_frame.pack(side="top", fill="both", expand=True)
t1.pack(side="top", fill="both", expand=True, ipady=5, ipadx=5)
t2.pack(side="top", fill="both", expand=True, pady=10, ipady=5, ipadx=5)
t3.pack(side="top", fill="both", expand=True, ipady=5, ipadx=5)
t4.pack(side="top", fill="both", expand=True)

# TAB 1 START
frame_tab_1 = ttk.Frame(main_frame)

# map display
map_frame = ttk.Frame(tab1, height=840, width=1150, )
map_canvas = tk.Canvas(map_frame, height=840, width=1150, borderwidth=0, highlightthickness=0,)
bg_img = ImageTk.PhotoImage(file="art/maps/map1.png")
map_canvas.create_image(0, 0, image=bg_img, anchor="nw", tag="map")
map_canvas.place(x=0, y=0)
# /map display
# /TAB1 END

# TAB2 START
frame_tab_2 = ttk.Frame(main_frame)

# tab2 is generated via 2 functions. scroll() which created the scrollable area and card_data()
# which injects the assets into scroll()

# /TAB2 END

tab_parent.grid(row=0, column=0)
frame_tab_1.grid(row=0, column=0)
frame_tab_2.grid(row=0, column=0)

menu_frame.grid(row=0, column=1, padx=55)
main_frame.pack(fill="both",expand=True)
map_frame.pack(fill="both",expand=True)

root.mainloop()