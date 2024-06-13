import pygame
import sys
from game import Game

# Constants
WIDTH, HEIGHT = 500, 620
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
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    screen.fill(DARK_BLUE)
    game.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
