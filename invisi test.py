import tkinter as tk
from random import randint

def levelOne():
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width = 500, height = 500, bg="white")
    canvas1.pack(fill = "both", expand = True)

    grid = tk.PhotoImage(file = "4X4.gif")
    img = tk.PhotoImage(file="player.gif")
    gridy = canvas1.create_image(10, 10, anchor=tk.NW, image=grid)
    image = canvas1.create_image(25, 60, anchor=tk.NW, image=img)
    turn = 0

    canvas1.create_text(400, 50, fill="black", font="Times 20", text="green = grass")
    canvas1.create_text(400, 100, fill="black", font="Times 20", text="brown = wood")
    canvas1.create_text(400, 200, fill="black", font="Times 20", text="Goals: ")
    canvas1.create_text(400, 250, fill="black", font="Times 20", text="Find Stalker")
    canvas1.create_text(400, 400, fill="black", font="Times 20", text="Turns: {}".format(turn))

    def move(event):
        "Move the arrow with a d w and s when clicked "
        if event.char == "a":
            canvas1.move(image, -55, 0)
        elif event.char == "d":
            canvas1.move(image, 55, 0)
        elif event.char == "w":
            canvas1.move(image, 0, -55)
        elif event.char == "s":
            canvas1.move(image, 0, 55)

    # This bind window to keys so that move is called when you press a key
    root.bind("<Key>", move)

    root.mainloop()


levelOne()
