
from individual import Individual

class Population(object):
    '''A population of individuals'''
    individuals = []

    def __init__(self, number):
        self.size = number

        for person in range(0, number):
            self.individuals.append(Individual(person))

    def draw(self, screen):
      """Draw a population on a pygame screen"""
      for person in self.individuals:
          person.draw(screen)

    def move(self):
      """Move a population"""
      for person in self.individuals:
          person.move()


