import pygame
from population import Population

class Region(object):
    '''A region with a population'''

    size = 0
    name = ""

    def __init__(self, name, number):
        self.size = number
        self.name = name
        self.population = Population(number)

    def draw(self, screen):
      """Draw a region on a pygame screen"""

      screen.fill((0, 0, 0))

      self.population.draw(screen)

    def iterate(self):
      """Iterate a region"""

      self.population.move()


