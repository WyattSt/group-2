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
 

def animate_player(Window, canvas,xinc,yinc):
  player = PhotoImage(file = "player.gif")
  canvas.create_image(25, 60, image = player, anchor = "nw")
  
  while True:
    canvas.move(player,xinc,yinc)
    Window.update()
    player_pos = canvas.coords(player)
    # unpack array to variables
    al,bl,ar,br = player_pos
    if al < abs(xinc) or ar > Window_Width-abs(xinc):
      xinc = -xinc
    if bl < abs(yinc) or br > Window_Height-abs(yinc):
      yinc = -yinc
 

Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_player(Animation_Window,Animation_canvas, Player_min_movement, Player_min_movement)

