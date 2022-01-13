###########################################################
#Names: Wyatt Stephens, RoShanda Dearborne, Joseph Newman
#Date: January 11, 2022
#Description: The Invisible Stalker
###########################################################
from tkinter import *
class titleScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setupGUI(self):
        TS = Label(self.master, text="The Invisible Stalker")
        TS.grid(row=0, column=3)

        b1 = Button(self.master, text="Tutorial")
        b1.grid(row=1, column=3)

        b2 = Button(self.master, text="Level 1")
        b2.grid(row=2, column=3)

        b3 = Button(self.master, text="Level 2")
        b3.grid(row=3, column=3)

        b4 = Button(self.master, text="Level 3")
        b4.grid(row=4, column=3)

class Tutorial(Frame):
    pass

class levelOne(titleScreen):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setupGUI(self):
        goal = Label(self.master, text="Goal: ")
        goal.grid(row=0, sticky="nes")

        g1 = Label(self.master, text="Find Stalker")
        g1.grid(row=1, sticky="nes")

        turns = Label(self.master, text="Turns Left: ")
        turns.grid(row=6, sticky="nes")

class levelTwo(titleScreen):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setupGUI(self):
        goal = Label(self.master, text="Goal: ")
        goal.grid(row=0, sticky="nes")

        g1 = Label(self.master, text="Find Sword")
        g1.grid(row=1, sticky="nes")

        g2 = Label(self.master, text="Find Stalker")
        g2.grid(row=2, sticky="nes")

        turns = Label(self.master, text="Turns Left: ")
        turns.grid(row=6, sticky="nes")

class levelThree(titleScreen):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setupGUI(self):
        goal = Label(self.master, text="Goal: ")
        goal.grid(row=0, sticky="nes")

        g1 = Label(self.master, text="Find Sword")
        g1.grid(row=1, sticky="nes")

        g2 = Label(self.master, text="Find Stalker")
        g2.grid(row=2, sticky="nes")

        g1 = Label(self.master, text="Find Key")
        g1.grid(row=3, sticky="nes")

        g1 = Label(self.master, text="Leave Through Door")
        g1.grid(row=4, sticky="nes")

        turns = Label(self.master, text="Turns Left: ")
        turns.grid(row=6, sticky="nes")

##### MAIN PROGRAM #####
window = Tk()
title = titleScreen(window)
title.setupGUI()
##l1 = levelOne(window)
##l1.setupGUI()
##l2 = levelTwo(window)
##l2.setupGUI()
##l3 = levelThree(window)
##l3.setupGUI()
window.mainloop()
