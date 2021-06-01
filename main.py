import pygame
pygame.init()
# win.create
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pokémon en python")

# boucle
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.QUIT()