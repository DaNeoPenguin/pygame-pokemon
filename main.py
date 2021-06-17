import pygame

class Game:
    def __init__(self):
        # win.create
        pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pokémon en python")


if __name__ == '__main__':
    pygame.init()
    game = Game()
    Game.run()
