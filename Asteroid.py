import pygame
import random
import os

BASE = os.path.dirname(os.path.abspath(__file__))

class Asteroid:
    def __init__(self):
        asteroidImag = pygame.image.load(f"{BASE}/static/asteroid.png")
        self.image = pygame.transform.scale(asteroidImag,(50,50))
        self.h = 50
        self.w = 50
        self.y = random.randint(108, 900 - 200 - self.h)
        randX = random.choice([0,1])
        if randX == 0:
            self.x = -50 - self.w
            self.xv = 8
        else:
            self.x = 1250 + 50
            self.xv = -8
 
    def draw(self, display):
        display.blit(self.image, (self.x, self.y) )

    def move(self):
        self.x += self.xv
