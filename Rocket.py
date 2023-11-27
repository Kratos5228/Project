import pygame
import os

BASE = os.path.dirname(os.path.abspath(__file__))

class Rocket():    
    def __init__(self, x):
        rocketImg = pygame.image.load(f"{BASE}/static/player01.png")
        self.image = pygame.transform.scale(rocketImg,(50,50))
        self.x = x 
        self.y = 790
        self.yv = 0
        self.w = 50
        self.h = 50
        self.score = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.y += self.yv

    def isCollision(self, rocks):
        if self.x < rocks.x + rocks.w and self.x + self.w > rocks.x + rocks.w:
            if self.y < rocks.y + rocks.h and self.y + self.h > rocks.y:
                return True

        if self.x + self.w > rocks.x and self.x < rocks.x:
            if self.y < rocks.y + rocks.h and self.y + self.h > rocks.y:
                return True
        
        if self.y > 850:
            return True

        return False

    def checkPoint(self):
        if self.y <= 100:
            self.score += 1
            self.y = 790

  