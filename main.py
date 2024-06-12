import pygame
import sys
from game import Game

# Constants
WIDTH, HEIGHT = 300, 600
FPS = 60
DARK_BLUE = (44, 44, 127)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(DARK_BLUE)
    game.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
