import tkinter
from tkinter import *
import time
 

Window_Width=800

Window_Height=600

Stalker_Start_XPosition = [25, 80, 135, 190]

Stalker_Start_YPosition = [25, 80, 135, 190]

Player_min_movement = 5

Refresh_Sec = 0.01
 

def create_animation_window():
  Window = tkinter.Tk()
  Window.title("The Invisible Stalker")

  Window.geometry(f'{Window_Width}x{Window_Height}')
  return Window
 

def create_animation_canvas(Window):
  canvas = tkinter.Canvas(Window)
  canvas.configure(bg="White")
  canvas.pack(fill="both", expand=True)
  return canvas
  grid = PhotoImage(file = "4X4.gif")
  gridy = canvas.create_image(10, 10, image = grid, anchor = "nw")
  Gridx1 = 25
  Gridx2 = 190
  Gridy1 = 60
  Gridy2 = 225
  
def animate_player(Window, canvas):
  x = [-55, 55]
  y = [-55, 55]
  player = PhotoImage(file = "player.gif")
  canvas.create_image(25, 60, image = player, anchor = "nw")
  def move(event):
    while True:
      if event.char == "a":
        canvas.move(player, -55, 0)
      elif event.char == "d":
        canvas.move(player, 55, 0)
      elif event.char == "w":
        canvas.move(player, 0, -55)
      elif event.char == "s":
        canvas.move(player, 0, 55)
    Window.update()
    player_pos = canvas.coords(player)
    # unpack array to variables
    al,bl,ar,br = player_pos
    if al <= Gridx2 or ar >= Gridx1:
      xinc = -xinc
    if bl <= Gridy2 or br >= Gridy1:
      yinc = -yinc
 

Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_player(Animation_Window, Animation_canvas)

