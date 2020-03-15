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

    # Attributes of the person
    name   = ""  # Unique name used to avoid self-infection
    age    = 40  # Can be used for survival rates and mobility
    size   = 5   # size in pixels

    # Position and direction of movement
    x  = 0
    y  = 0
    dx = 0
    dy = 0

    infected      = False  # Infected even if not known
    alive         = True   # Alive or dead
    quarantined   = False  # Quarantined or not.  Affect movement
    infected_time = 0      # Time of infection
    immune        = False  # People become immune after recovery
    symptomatic   = False  # Does the person suspect they are sick
    diagnosed     = False  # Has it been confirmed the person is sick

    def __init__(self, name, size):
        self.name = str(name)
        self.age  = int(gauss(0, 50) + 50)

        # Initialize a position and a velocity vector
        self.x    = randint(0, size)
        self.y    = randint(0, size)
        self.dx   = random() * 4 - 2
        self.dy   = random() * 4 - 2

        # Randomly infect at start (could be passed in)
        if randint(0, 100) < 2:
            self.infected = True
            infected_time = pygame.time.get_ticks()
        else:
            self.infected = False

    def draw(self, screen):
          
          # Dead      = red
          # Recovered = blue
          # Infected  = magenta
          # Healthy   = green
          if (not self.alive):  color = (255,  0,  0)
          elif (self.immune):   color = (  0,  0,255)
          elif (self.infected): color = (255,  0,255)
          else:                 color = (  0,255,  0)

          pygame.draw.ellipse(screen, color, 
                    pygame.Rect(self.x - self.size / 2, 
                                self.y - self.size / 2,
                                self.size, self.size))

    # Move a person.
    def move(self, size):
        # If dead or under quarantine, do not move
        if self.alive and not self.quarantined:
            self.x = self.x + self.dx
            self.y = self.y + self.dy

            # Test for boundary collisions.  If over 
            # the borders, undo previous move and add
            # additional movement.  Reverse the direction
            # vector based on what side we hit
            if (self.x > size) or (self.x < 0):
                self.x = self.x - self.dx * 2
                self.dx = -self.dx

            if (self.y > size) or (self.y < 0):
                self.y = self.y - self.dy * 2
                self.dy = -self.dy

    # Test for recovery, death, and symptoms
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

    # Try to see who should be infected
    def infect(self, population, virus):
        # Only test the living, healthy and not immune
        if self.alive and not self.infected and not self.immune:

            # Find anybody we are colliding with
            for person in population:
                if person.name != self.name and person.infected:

                    # Calculate the distance apart
                    distance = sqrt((self.x - person.x) ** 2 +
                                    (self.y - person.y) ** 2)

                    # If the distance is less than our size (radius) and
                    # the infection distance of this virus, roll the dice
                    if distance < (self.size + virus.infection_distance):
                        if (random() < virus.infection_prob):
                            self.infected = True
                            self.infected_time = pygame.time.get_ticks()

        # Check for quarantine
        #
        # If I am alive and infected and not ytet
        if self.alive and self.infected:
            if self.infected and not self.symptomatic and not self.quarantined:
                if virus.test_symptomatic(
                        self.age,
                        pygame.time.get_ticks() - self.infected_time):
                    self.quarantined = True


