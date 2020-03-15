import pygame
from region import Region
from virus  import Virus
import random
from datetime import datetime

pygame.init()
done = False
clock = pygame.time.Clock()

regions = []

myvirus = Virus("test", 0.03, 5, 14000, 0.97, 5000) 

regions.append(Region("region1", 100, 500, myvirus))


timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 50)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == timer_event:
            for myregion in regions:
              myregion.draw()
              myregion.iterate()

        pygame.display.flip()

