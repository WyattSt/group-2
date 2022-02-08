import pygame as pg
import sys
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        pass

    # For creating sprites, walls, etc.
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 1, 1)

        # BOUNDARIES
        for x in range(0, 4):       
            Wall(self, x, -1)       #top boundary

        for x in range(0, 4):
            Wall(self, x, 4)        #bottom boundary

        for x in range(-1, 0):
            for y in range(0,4):
                Wall(self, x, y)    #left boundary

        for x in range(4, 9):
            for y in range(0, 4):
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
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    # Take user input ( WASD for movement )
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_a:
                    self.player.move(dx = -1)
                if event.key == pg.K_d:
                    self.player.move(dx = 1)
                if event.key == pg.K_w:
                    self.player.move(dy = -1)
                if event.key == pg.K_s:
                    self.player.move(dy = 1)


# Start the game
g = Game()

while True:
    g.new()
    g.run()

