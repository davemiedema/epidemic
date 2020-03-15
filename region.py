import pygame
from population import Population
from virus      import Virus

class Region(object):
    '''A region with a population'''

    size = 0
    name = ""

    def __init__(self, name, number, virus):
        self.size = number
        self.name = name
        self.population = Population(number)
        self.virus = virus


    def draw(self, screen):
      """Draw a region on a pygame screen"""

      screen.fill((0, 0, 0))

      self.population.draw(screen)

    def iterate(self):
      """Iterate a region"""

      self.population.move()
      self.population.infect(self.virus)
      self.population.cure(self.virus)


