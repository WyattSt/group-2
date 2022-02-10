import pygame as pg

# Define any colors that we want to use
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WOOD = (93, 79, 57)

# Sets the size of the window
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "The Invisible Stalker"
BGCOLOR = DARKGREY

# 4x4 Grid
GRIDx = 512
GRIDy = 512

# Set size of the tiles
TILESIZE = 128
GRIDWIDTH = GRIDx / TILESIZE
GRIDHEIGHT = GRIDy / TILESIZE

# Audio
BG_MUSIC = 'rats.ogg'
EFFECTS_SOUNDS = {'woodabove': 'woodabove.wav'}

