import pygame

pygame.init()




def run():
    # boucle
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                var = pygame.QUIT
