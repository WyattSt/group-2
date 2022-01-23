from tkinter import *
from random import randint

root = Tk()

root.geometry("500x500")

image1 = PhotoImage(file = "4X4.gif")
resize_image1 = image1.resize((100, 100))
grid = ImageTk.PhotoImage(resize_image1)

player = PhotoImage(file = "arrow.gif")

canvas1 = Canvas(root, width = 500, height = 500, bg="white")
canvas1.pack(fill = "both", expand = True)

canvas1.create_image(10, 10, image = grid, anchor = "nw")
canvas1.create_image(0, 0, image = player, anchor = "nw")


canvas1.create_text(400, 50, fill="black", font="Times 20 italic bold", text="green = grass")
canvas1.create_text(400, 100, fill="black", font="Times 20 italic bold", text="brown = wood")
canvas1.create_text(400, 200, fill="black", font="Times 20 italic bold", text="Goals: ")
canvas1.create_text(400, 250, fill="black", font="Times 20 italic bold", text="Find Stalker")
canvas1.create_text(400, 400, fill="black", font="Times 20 italic bold", text="Turns: ")

root.mainloop()

