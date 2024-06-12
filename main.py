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

drop_ms = 200
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, drop_ms)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()
        if event.type == GAME_UPDATE:
            game.move_down()

    screen.fill(DARK_BLUE)
    game.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
