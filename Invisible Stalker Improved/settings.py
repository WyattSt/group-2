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
DARKGREEN = (0, 76 ,0)

# Sets the size of the window
WIDTH = 782
HEIGHT = 512
FPS = 60
TITLE = "The Invisible Stalker"
BGCOLOR = DARKGREY

# 4x4 Grid
GRIDx = 512
GRIDy = 512

# Set size of the tiles
TILESIZE = 84
GRIDWIDTH = GRIDx / TILESIZE
GRIDHEIGHT = GRIDy / TILESIZE

# Audio
EFFECTS_SOUNDS = {'woodabove': 'woodabove.wav', 'woodleft': 'woodleft.wav',
                  'woodright': 'woodright.wav', 'woodbehind': 'woodbehind.wav',
                  'grassabove': 'grassabove.wav', 'grassleft': 'grassleft.wav',
                  'grassright': 'grassright.wav', 'grassbehind': 'grassbehind.wav'}

