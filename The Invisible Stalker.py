###########################################################
#Names: Wyatt Stephens, RoShanda Dearborne, Joseph Newman
#Date: January 11, 2022
#Description: The Invisible Stalker
###########################################################
import tkinter
from tkinter import *
from random import randint

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

class Tutorial(titleScreen):
    pass

class levelOne(titleScreen):
    def __init__(self, parent):
        titleScreen.__init__(self, parent)

    def setupGUI(self):        
        self.pack(fill=BOTH, expand=1)
        
        img = None
        levelOne.image = Label(self, width=WIDTH // 2, image=img)
        levelOne.image.image = img
        levelOne.image.pack(side=LEFT, fill=Y)
        levelOne.image.pack_propagate(False)

        text_frame = Frame(self, width=WIDTH // 2)
        levelOne.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        levelOne.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    def setGridImage(self):
        levelOne.img = PhotoImage(file="4X4.gif")

        levelOne.image.config(image=levelOne.img)
        levelOne.image.image = levelOne.img

    def setStatus(self, turns):
        turns = 0
        levelOne.text.config(state=NORMAL)

        levelOne.text.insert(END, "Level One." +\
                             "\nGoals: " + "\nFind Stalker" +\
                             "\n\nTurns Left: {}".format(turns))
        levelOne.text.config(state=DISABLED)
        

    def play(self):
        self.setupGUI()
        self.setGridImage
        self.setStatus("")
    


    def player():
        pass

    def stalker():
        pass

    def floorMaterials():
        pass

    

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
WIDTH = 800
HEIGHT = 600

window = Tk()
window.title("The Invisible Stalker")
##title = titleScreen(window)
##title.setupGUI()
l1 = levelOne(window)
l1.play()
##l2 = levelTwo(window)
##l2.setupGUI()
##l3 = levelThree(window)
##l3.setupGUI()
window.mainloop()
