from random import random

class Virus(object):
    '''A virus'''
    name = "virus"
    infection_prop = 0.50
    infection_distance = 5
    life_expectancy = 3000

    def __init__(self, name, prob, dist, life_exp, recovery, incubation):
        self.name               = name
        self.infection_prob     = prob
        self.infection_distance = dist
        self.life_expectancy    = life_exp
        self.recovery_prob      = recovery
        self.incubation         = incubation

    def test_dead(self, age, duration):
        if duration > self.life_expectancy:
            return random() > self.recovery_prob
        else:
            return False

    def test_cured(self, age, duration):
        if duration > self.life_expectancy:
            return random() < self.recovery_prob
        else:
            return False

    def test_symptomatic(self, age, duration):
        if duration > self.incubation:
            return True
        else:
            return False

