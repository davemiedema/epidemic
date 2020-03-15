
from individual import Individual

class Population(object):
    '''A population of individuals'''
    individuals = []

    def __init__(self, number, size):
        self.number = number

        for person in range(0, number):
            individual = Individual(person, size) 

            if person == 0:
                individual.infected = True

            self.individuals.append(individual)

    def draw(self, screen):
      """Draw a population on a pygame screen"""
      for person in self.individuals:
          person.draw(screen)

    def move(self, size):
      """Move a population"""
      for person in self.individuals:
          person.move(size)

    def infect(self, virus):
      """Move a population"""
      for person in self.individuals:
          person.infect(self.individuals, virus)
      
    def cure(self, virus):
      """Cure a population"""
      for person in self.individuals:
          person.cure(self.individuals, virus)

      


