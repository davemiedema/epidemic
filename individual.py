import pygame
from random import seed
from random import gauss
from random import randint
from random import random
from math   import sqrt
from virus  import Virus

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
    size = 5
    infected_time = 0
    immune = False
    symptomatic = False

    def __init__(self, name):
        self.name = str(name)
        self.age  = int(gauss(0, 50) + 50)
        self.x    = randint(0, 400)
        self.y    = randint(0, 300)
        self.dx   = random() * 4 - 2
        self.dy   = random() * 4 - 2

        if randint(0, 100) < 2:
            self.infected = True
            infected_time = pygame.time.get_ticks()
        else:
            self.infected = False

    def draw(self, screen):
          color = (255, 255, 0)
          if (not self.alive): color = (255,0,0)
          elif (self.immune): color = (0,0,255)
          elif (self.infected): color = (255,255,0)
          else: 
              color = (0, 255, 0)

          pygame.draw.ellipse(screen, color, 
                    pygame.Rect(self.x - self.size / 2, 
                                self.y - self.size / 2,
                                self.size, self.size))

    def move(self):
        if self.alive and not self.quarantined:
            self.x = self.x + self.dx
            self.y = self.y + self.dy

            if (self.x > 400) or (self.x < 0):
                self.x = self.x - self.dx * 2
                self.dx = -self.dx

            if (self.y > 300) or (self.y < 0):
                self.y = self.y - self.dy * 2
                self.dy = -self.dy

    def cure(self, population, virus):
        if self.alive and self.infected:
            if virus.test_cured(self.age, 
                  pygame.time.get_ticks() - self.infected_time):
                self.infected    = False
                self.immune      = True
                self.quarantined = False
            elif virus.test_dead(self.age, 
                  pygame.time.get_ticks() - self.infected_time):
                self.alive    = False
                self.infected = False
            elif virus.test_symptomatic(self.age, 
                  pygame.time.get_ticks() - self.infected_time):
                self.symptomatic = True

    def infect(self, population, virus):
        if self.alive and not self.infected and not self.immune:
            for person in population:
                if person.name != self.name and person.infected:
                    distance = sqrt((self.x - person.x) ** 2 +
                                    (self.y - person.y) ** 2)
                    if distance < (self.size + virus.infection_distance):
                        if (random() < virus.infection_prob):
                            self.infected = True
                            self.infected_time = pygame.time.get_ticks()

        if self.alive and self.infected:
            if self.infected and not self.symptomatic and not self.quarantined:
                if virus.test_symptomatic(
                        self.age,
                        pygame.time.get_ticks() - self.infected_time):
                    self.quarantined = True


