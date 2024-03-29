import pygame as pg
import sys
from settings import * 
from sprites import *
from tilemap import *
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
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'map1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.grass_img = pg.image.load(path.join(img_folder, GRASS_IMG)).convert_alpha()
        self.grass_img = pg.transform.scale(self.grass_img, (TILESIZE,TILESIZE))
        self.nobg_img = pg.image.load(path.join(img_folder, NOBG_IMG)).convert_alpha()
        self.nobg_img = pg.transform.scale(self.nobg_img, (TILESIZE,TILESIZE))
        self.wood_img = pg.image.load(path.join(img_folder, WOOD_IMG)).convert_alpha()
        self.wood_img = pg.transform.scale(self.wood_img, (TILESIZE,TILESIZE))
        self.hud_font = path.join(img_folder, 'Quicksand-SemiBold.ttf')

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
        self.grass = pg.sprite.Group()
        self.wood = pg.sprite.Group()
        self.player = Player(self, 1, 1)
        self.stalker = Stalker(self, random.choice([i for i in range(0,3) if i not in[1]]) , random.choice([i for i in range(0,3) if i not in [1]]))
##        for row, tiles in enumerate(self.map.data):
##            for col, tile in enumerate(tiles):
##                if tile == 'G':
##                    Grass(self, col, row)
##                if tile == 'W':
##                    Wood(self, col, row)
        
        
##
##        # BOUNDARIES
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

    # Draws a grid to help show tiles
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, GRIDx))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (GRIDy, y))

    # Draw function
    def draw(self):
##        self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, (1,1))
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text('Turns Left: {}'.format(turn), self.hud_font, 50, WHITE, WIDTH - 80, 10, align="ne")
        if turn == 0:
            self.draw_text('Game Over: Out of Turns', self.hud_font, 70, WHITE, WIDTH/2, HEIGHT - 125, align="center")
        if self.player.rect.colliderect(self.stalker):
            global stalker_found
            stalker_found = 1
            self.draw_text('Stalker Found!', self.hud_font, 70, WHITE, WIDTH/2, HEIGHT - 125, align="center")
        pg.display.flip()

    # Take user input ( WASD for movement )
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                global turn
                global stalker_found
                if turn > 0 and stalker_found == 0:
                    if event.key == pg.K_ESCAPE:
                        self.quit()
                    if event.key == pg.K_a:
                        self.player.move(dx = -1)
                        self.stalker.move(dy = random.choice([-1, 1]))
                        turn += -1
                    if event.key == pg.K_d:
                        self.player.move(dx = 1)
                        self.stalker.move(dx = random.choice([-1, 1]))
                        turn += -1
                    if event.key == pg.K_w:
                        self.player.move(dy = -1)
                        self.stalker.move(dy = random.choice([-1, 1]))
                        turn += -1
                    if event.key == pg.K_s:
                        self.player.move(dy = 1)
                        self.stalker.move(dx = random.choice([-1, 1]))
                        turn += -1

# Start the game
g = Game()
turn = 20
stalker_found = 0

while True:
    g.new()
    g.run()

