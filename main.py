import pygame
import sys
import random
import math

class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super(Basket,self).__init__()
        self.x = 325
        self.y = 600
        self.image = pygame.image.load("basket2.png").convert_alpha()
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.image = pygame.transform.scale(self.image, (100,70))

    def move(self, deltax, deltay):
        if self.rect.left < 0 or self.rect.right>650:
            deltax *= -3
        if self.rect.top < 0 or self.rect.bottom > 600:
            deltay *= -3

        self.rect.centerx += deltax
        self.rect.centery += deltay


class Chick(pygame.sprite.Sprite):
    def __init__(self):
        self.x = random.randint(60,590)
        self.y = random.randint(60,200)
        yellow_files = ["yellow/chickwingsdown.png","yellow/chickwingsup.png"]
        self.pics = [pygame.image.load(img) for img in yellow_files]
        self.image = self.pics[0]
        self.rect = self.image.get_rect(center=(self.x,self.y))

    def move(self,deltax,deltay):
        self.rect.centerx += deltax
        self.rect.centery += deltay







# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create clock to later control frame rate
clock = pygame.time.Clock()


basket = Basket()
baskets = pygame.sprite.Group()
baskets.add(basket)

chicks = pygame.sprite.Group()
for i in range(5):
    chicks.add(Chick())
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill(WHITE)

        # Get the state of all keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket.move(-2,0)
    if keys[pygame.K_RIGHT]:
        basket.move(2,0)

    for chick in chicks:
        chick.move(0,-1)
    
    baskets.draw(screen)
    chicks.draw(screen)
    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(30)

# Quit Pygame properly
pygame.quit()
sys.exit()
