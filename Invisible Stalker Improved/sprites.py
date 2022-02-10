import pygame as pg
from settings import *

# Define what the player is/what it can do
class Player(pg.sprite.Sprite):
    def __init__(self, game, x , y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    # Checks to see if a wall is in the way
    def move(self, dx= 0, dy = 0):
        if not self.wall_collision(dx, dy):
            self.x += dx
            self.y += dy
            
    # Wall collision detector
    def wall_collision(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    # Update player rect location
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE     


        
# Defining the Stalker
class Stalker(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def wall_collision(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def grass_detection(self, dx = 0, dy = 0):
        for grass in self.game.grass_tiles:
            if grass.x == self.x and grass.y == self.y:
                return True
        False



    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def move(self, dx = 0, dy = 0):
        if not self.wall_collision(dx, dy):
            self.x += dx
            self.y += dy

        if self.grass_detection(dx, dy):
            #self.effects_sound['woodabove'].play()
            pass
        

# Defines what a wall is 
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x ,y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Grass(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.grass_tiles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WOOD)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE



