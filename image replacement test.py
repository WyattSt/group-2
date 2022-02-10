import  pygame
                        
# width
width = 680
  
# height
height = 480
  
#store he screen size
z = [width,height]
  
# store the color
white = (255, 255, 255)
screen_display = pygame.display

image_one = pygame.image.load('tile_01.png')
image_two = pygame.image.load('tile_46.png')

class MyImage:
    def __init__(self, x, y):
        pygame.init()
        self.x = x
        self.y = y
        self.images = ["image_one", "image_two"]
        self.c = 0

    def onSpace(self):
        self.c = (self.c + 1) % len(self.images)

    def get_image(self):
        return self.images[self.c]
    
        stopped = False
        while stopped == False:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        test_image.onSpace()
                        
# Set caption of screen
screen_display.set_caption('GEEKSFORGEEKS')
  
# setting the size of the window
surface = screen_display.set_mode(z)
  
# set the image which to be displayed on screen
test_image = MyImage(50, 50)
image_one = pygame.image.load('tile_01.png')
image_two = pygame.image.load('tile_46.png')

surface.fill(white)
     
# draw on image onto another
pygame.surface.blit(test_image.get_image(), (test_image.x, test_image.y))
screen_display.update()
