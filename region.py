import pygame
from population import Population
from virus      import Virus

class Region(object):
    '''A region with a population'''

    number = 0
    name = ""
    size = 400
    screen = None

    def __init__(self, name, number, size, virus):
        self.number     = number
        self.name       = name
        self.population = Population(number, size)
        self.virus      = virus
        self.size       = size
        self.screen     = pygame.display.set_mode((size,size)) 

    def draw(self):
      """Draw a region on a pygame screen"""

      self.screen.fill((0, 0, 0))

      self.population.draw(self.screen)

    def iterate(self):
      """Iterate a region"""

      self.population.move(self.size)
      self.population.infect(self.virus)
      self.population.cure(self.virus)


