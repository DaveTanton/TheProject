
from tkinter import *

class test_class:

    def __init__(self):
        self.p_lst=p_lst = [
                            ({'name': 'Tom', 'vp': 2 }),
                            ({'name': 'Dick', 'vp': 0}),
                            ({'name': 'Harry', 'vp': 2}),
                            ({'name': 'Jane', 'vp': 0}),
                            ({'name': 'Dick', 'vp': 0}),
                            ({'name': 'Harry', 'vp': 2}),
                            ({'name': 'Jane', 'vp': 0}),
                            ({'name': 'RED', 'vp': 2}),
                            ({'name': 'GREEN', 'vp': 0}),
                            ({'name': 'BLUE', 'vp': 2}),
                            ({'name': 'YELLOW', 'vp': 0}),
                            ({'name': 'PINK', 'vp': 0}),
                            ({'name': 'WHITE', 'vp': 2}),
                            ({'name': 'CYAN', 'vp': 0})
                            ]

    def test_col_row(self):
        for i in range(len(self.p_lst)):
            self.p_card(self.p_lst[i])
            for j in range(3):
                self.card_frame.grid(column=i, row=j, padx=5, pady=5)

    def p_card(self,a_lst):
        self.card_frame = LabelFrame(viewport, text="Card")
        name_label = Label(self.card_frame, text="planet name: " + a_lst["name"])
        vp_label = Label(self.card_frame, text="VP:" + str(a_lst["vp"]))

        name_label.grid(column=0, row=1)
        vp_label.grid(column=0, row=2)

class AutoGrid(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.columns = None
        self.bind('<Configure>', self.regrid)
        print("AUTOGRID")

    def regrid(self, event=None):
        width = self.winfo_width()
        slaves = self.grid_slaves()
        max_width = max(slave.winfo_width() for slave in slaves)
        cols = width // max_width
        if cols == self.columns: # if the column number has not changed, abort
            return
        for i, slave in enumerate(slaves):
            slave.grid_forget()
            slave.grid(row=i//cols, column=i%cols)
        self.columns = cols
        print("REGRID")


root = Tk()


viewport=AutoGrid(root)
viewport.pack(fill=BOTH, expand=True)

alpha=test_class()
alpha.test_col_row()

root.mainloop()
