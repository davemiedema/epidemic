import pygame
from region import Region

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
clock = pygame.time.Clock()

myregion = Region("my region", 10)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        myregion.draw(screen)
        myregion.iterate()

        pygame.display.flip()
        clock.tick(60)

