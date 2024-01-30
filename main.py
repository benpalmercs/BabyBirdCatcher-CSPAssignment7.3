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
        
        self.rect.centerx += deltax


class Chick(pygame.sprite.Sprite):
    def __init__(self):
        super(Chick,self).__init__()
        self.speed = 1
        self.x = random.randint(60,300)
        self.y = random.randint(60,200)
        yellow_files = ["yellow/chickwingsdown.png","yellow/chickwingsup.png"]
        self.pics = [pygame.image.load(img) for img in yellow_files]
        self.index = 0
        self.image = self.pics[0]
        self.image = pygame.transform.scale(self.image, (70,60))
        self.rect = self.image.get_rect(center=(self.x,self.y))

    def move(self,deltax,deltay):
        self.index+=1
        self.image = self.pics[self.index%2]
        self.image = pygame.transform.scale(self.image, (70,60))
        self.rect.centerx += deltax
        self.rect.centery += deltay*self.speed

    def relocate(self):
        self.rect = self.image.get_rect(center=(random.randint(60, 300), random.randint(60,200)))

   





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

# Setting up Sprite Groups
basket = Basket()
baskets = pygame.sprite.Group()
baskets.add(basket)

chicks = pygame.sprite.Group()
for i in range(5):
    chicks.add(Chick())

# Creating Score Values
dropped = 0
points = 0

# Setting up Font Surfaces for Scoreboard
font = pygame.font.SysFont(None, 32)
score = font.render("Score: " + str(points), True, BLUE)
screen.blit(score, (20, 20))



# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill(WHITE)
    score = font.render("Score: " + str(points), True, BLUE)
    screen.blit(score, (0, 0))
        # Get the state of all keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket.move(-4,0)
        
    if keys[pygame.K_RIGHT]:
        basket.move(4,0)

    for chick in chicks:
        if points>10:
            chick.speed = points/10
        chick.move(0,1)
        # if chick.rect.colliderect(basket.rect):
        if chick.rect.bottom < 520:
            if pygame.sprite.collide_mask(chick,basket):
                points += 1
                chick.relocate()

        if chick.rect.bottom > 600:
            dropped += 1
            chick.relocate()

    
    baskets.draw(screen)
    chicks.draw(screen)
    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(30)

# Quit Pygame properly
pygame.quit()
sys.exit()
