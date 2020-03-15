import pygame
from random import seed
from random import gauss
from random import randint
from random import random

seed(1)

class Individual(object):
    '''An individual'''
    name = ""
    age = 40
    infected = False
    recovered = False
    alive = True
    x = 0
    y = 0
    quarantined = False
    diagnosed = False
    dx = 0
    dy = 0

    def __init__(self, name):
        self.name = str(name)
        self.age  = int(gauss(0, 50) + 50)
        self.x    = randint(0, 400)
        self.y    = randint(0, 300)
        self.dx   = random() * 4 - 2
        self.dy   = random() * 4 - 2

    def draw(self, screen):
          pygame.draw.ellipse(screen, (255,255,0), 
                    pygame.Rect(self.x, self.y, 5, 5))

    def move(self):
        if self.alive and not self.quarantined:
            self.x = self.x + dx
            self.y = self.y + dy

