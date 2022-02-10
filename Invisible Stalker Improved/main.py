import pygame as pg
import sys
from settings import * 
from sprites import *
from os import path
import random


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        snd_folder = path.join(game_folder, 'snd')
        music_folder = path.join(game_folder, 'music')
        self.hud_font = path.join(img_folder, 'Quicksand-SemiBold.ttf')
        # Sound load
        self.effects_sounds = {}
        for type in EFFECTS_SOUNDS:
            self.effects_sounds[type] = pg.mixer.Sound(path.join(snd_folder, EFFECTS_SOUNDS[type]))

    # function for drawing text on screen
    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    # For creating sprites, walls, etc.
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.wood_tiles = pg.sprite.Group()
        self.grass_tiles = pg.sprite.Group()
        self.stalker = Stalker(self, random.choice([i for i in range(0,4) if i not in[1]]) , random.choice([i for i in range(0,4) if i not in [1]]))
        
        # WALL PLACEMENT
        for x in range(0, 4):       
            Wall(self, x, -1)       #top boundary

        for x in range(0, 4):
            for y in range(4, 6):
                Wall(self, x, y)    #bottom boundary

        for x in range(-1, 0):
            for y in range(0,4):
                Wall(self, x, y)    #left boundary


        for x in range(8, 9):       
            for y in range(0, 6):
                Wall(self, x, y)    #right boundary

        for x in range(4, 9):
            for y in range(0, 6):
                Wall(self, x, y)

        # WOOD PLACEMENT
        for x in range(1, 4):
            for y in range(1, 2):
                Wood(self, x ,y)

        for x in range(1, 4):
            for y in range(3, 4):
                Wood(self, x ,y)

        for x in range(0,1):
            for y in range(2,3):
                Wood(self, x, y)

        for x in range(2, 3):
            for y in range(0,1):
                Wood(self, x, y)

        for x in range(2, 3):
            for y in range(2,3):
                Wood(self, x, y)

        # GRASS PLACEMENT
        for x in range(0, 2):
            for y in range(0,1):
                Grass(self, x, y)

        for x in range(0, 1):
            for y in range(0,1):
                Grass(self, x, y)

        for x in range(0, 1):
            for y in range(1,2):
                Grass(self, x, y)
                
        for x in range(0, 1):
            for y in range(3,4):
                Grass(self, x, y)

        for x in range(3, 4):
            for y in range(0,1):
                Grass(self, x, y)

        for x in range(1, 2):
            for y in range(2,3):
                Grass(self, x, y)

        for x in range(3, 4):
            for y in range(2,3):
                Grass(self, x, y)
                
        self.player = Player(self, 1, 1)
        #self.stalker = Stalker(self, random.choice([i for i in range(0,4) if i not in[1]]) , random.choice([i for i in range(0,4) if i not in [1]]))



    # Continually update whats on screen
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

    # Quit Function
    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

        # Stalker touches wood, plays sound according to direction

        global play_sound
        if self.stalker.wood_detection() == True and play_sound == True:
            if (self.stalker.y == self.player.y - 1) and (self.stalker.x == self.player.x):
                self.effects_sounds['woodabove'].play()
                play_sound = False
                
        if self.stalker.wood_detection() == True and play_sound == True:
            if (self.stalker.y == self.player.y) and (self.stalker.x + 1 == self.player.x):
                self.effects_sounds['woodleft'].play()
                play_sound = False
                
        if self.stalker.wood_detection() == True and play_sound == True:
            if (self.stalker.y == self.player.y) and (self.stalker.x - 1 == self.player.x):
                self.effects_sounds['woodright'].play()
                play_sound = False

        if self.stalker.wood_detection() == True and play_sound == True:
            if (self.stalker.y == self.player.y + 1) and (self.stalker.x == self.player.x):
                self.effects_sounds['woodbehind'].play()
                play_sound = False
                
        # Stalker touches grass, play sound according to direction

        if self.stalker.grass_detection() == True and play_sound == True:
            if (self.stalker.y == self.player.y - 1) and (self.stalker.x == self.player.x):
                self.effects_sounds['grassabove'].play()
                play_sound = False
                
        if self.stalker.grass_detection() == True and play_sound == True:
            if (self.stalker.y == self.player.y) and (self.stalker.x + 1 == self.player.x):
                self.effects_sounds['grassleft'].play()
                play_sound = False
                
        if self.stalker.grass_detection() == True and play_sound == True:
            if (self.stalker.y == self.player.y) and (self.stalker.x - 1 == self.player.x):
                self.effects_sounds['grassright'].play()
                play_sound = False

        if self.stalker.grass_detection() == True and play_sound == True:
            if (self.stalker.y == self.player.y + 1) and (self.stalker.x == self.player.x):
                self.effects_sounds['grassbehind'].play()
                play_sound = False

    # Draws a grid to help show tiles
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, GRIDx))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (GRIDy, y))

    # Draw function
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text('Turns Left: {}'.format(turn), self.hud_font, 50, WHITE, WIDTH - 80, 10, align="ne")
        if turn == 0:
            self.draw_text('Game Over: Out of Turns', self.hud_font, 50, WHITE, WIDTH/2, HEIGHT - 125, align="center")
        if self.player.rect.colliderect(self.stalker):
            global stalker_found
            global objective
            stalker_found = 1
            self.draw_text('Stalker Found!', self.hud_font, 70, WHITE, WIDTH/2, HEIGHT - 125, align="center")
        self.draw_text("Objective: ", self.hud_font, 50, WHITE, WIDTH - 100, 90, align="ne")
        if stalker_found == 1:
            self.draw_text("", self.hud_font, 50, WHITE, WIDTH - 90, 150, align="ne")
        else: self.draw_text("{}".format(objective), self.hud_font, 50, WHITE, WIDTH - 90, 150, align="ne")
        pg.display.flip()

    # Take user input ( WASD for movement )
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                global turn
                global stalker_found
                global play_sound
                if turn > 0 and stalker_found == 0:
                    if event.key == pg.K_ESCAPE:
                        self.quit()
                    if event.key == pg.K_a:
                        self.player.move(dx = -1)
                        self.stalker.move(dy = random.choice([-1, 1]))
                        turn += -1
                        play_sound = True
                    if event.key == pg.K_d:
                        self.player.move(dx = 1)
                        self.stalker.move(dx = random.choice([-1, 1]))
                        turn += -1
                        play_sound = True
                    if event.key == pg.K_w:
                        self.player.move(dy = -1)
                        self.stalker.move(dy = random.choice([-1, 1]))
                        turn += -1
                        play_sound = True
                    if event.key == pg.K_s:
                        self.player.move(dy = 1)
                        self.stalker.move(dx = random.choice([-1, 1]))
                        turn += -1
                        play_sound = True


# Start the game
g = Game()

turn = 20
stalker_found = 0
objective = "Find Stalker"
play_sound = True

while True:
    g.new()
    g.run()

