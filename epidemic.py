import pygame
from region import Region
from virus  import Virus

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
clock = pygame.time.Clock()

myregion = Region("my region", 100, Virus("test", 0.01, 30, 14000, 0.68, 5000))


timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 50)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == timer_event:
            myregion.draw(screen)
            myregion.iterate()

        pygame.display.flip()

