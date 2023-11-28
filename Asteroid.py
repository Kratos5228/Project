import pygame
import random
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# Class for the Asteroid
class Asteroid:
    def __init__(self):
        asteroidImag = pygame.image.load(f"{BASE}/static/asteroid.png")
        self.image = pygame.transform.scale(asteroidImag,(50,50))
        self.h = 50
        self.w = 50
        # Creates space between the end if the window and the moving asteroids 
        # as well as the beginning so the rocket won't get hit at the top or bottom
        self.y = random.randint(108, 900 - 150 - self.h)
        # randX will pick from choice 0 and 1
        randX = random.choice([0,1])
        # if it chooses 0 the asteroids will be coming from the left to right
        if randX == 0:
            self.x = -100 - self.w         
            self.xv = 8                    # has a positive velocity to move right
        # if it chooses 1 the asteroids will be coming from the right to left
        else:
            self.x = 1250 + 50             # spawns the asteroid at 1300 on x
            self.xv = -8                   # has a negative velocity to move left
 
    def draw(self, display):
        display.blit(self.image, (self.x, self.y) )

    def move(self):
        self.x += self.xv
