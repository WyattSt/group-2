import tkinter as tk
 
# Create the window with the Tk class
root = tk.Tk()
 
# Create the canvas and make it visible with pack()
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack() # this makes it visible
 
# Loads and create image (put the image in the folder)
grid = tk.PhotoImage(file = "4X4.gif")
img = tk.PhotoImage(file="arrow2.gif")
gridy = canvas.create_image(10, 10, anchor=tk.NW, image=grid)
image = canvas.create_image(10, 10, anchor=tk.NW, image=img)
 
def move(event):
    """Move the sprite image with a d w and s when click them"""
    if event.char == "a":
        canvas.move(image, -200, 0)
    elif event.char == "d":
        canvas.move(image, 200, 0)
    elif event.char == "w":
        canvas.move(image, 0, -200)
    elif event.char == "s":
        canvas.move(image, 0, 200)
 
# This bind window to keys so that move is called when you press a key
root.bind("<Key>", move)
 
# this creates the loop that makes the window stay 'active'
root.mainloop()
