import pygame
from population import Population
from virus      import Virus

class Region(object):
    '''A region with a population'''

    number = 0     ## Size of population in the region
    name   = ""    ## Name of the region
    size = 400     ## Physical size in pixels
    screen = None  ## Screen to draw on

    def __init__(self, name, number, size, virus):
        self.number     = number
        self.name       = name
        self.population = Population(number, size)
        self.virus      = virus
        self.size       = size
        self.screen     = pygame.display.set_mode((size,size)) 

    def draw(self):
      """Draw a region on a pygame screen"""

      # Clear the screen before redrawing
      self.screen.fill((0, 0, 0))

      # Draw the population
      self.population.draw(self.screen)

    def iterate(self):
      """Iterate a region"""

      # Move the population, test for infection, test for cures and death
      self.population.move(self.size)
      self.population.infect(self.virus)
      self.population.cure(self.virus)


