import pygame
import sys
from game import Game

# Constants
WIDTH, HEIGHT = 500, 620
FPS = 60
DARK_BLUE = (44, 44, 127)
LIGHT_BLUE = (100, 100, 255)
WHITE = (255, 255, 255)

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, WHITE)
level_surface = title_font.render("Level", True, WHITE)
next_surface = title_font.render("Next", True, WHITE)
gameover_surface = title_font.render("GAME OVER", True, WHITE)

score_y = 20
level_y = 130
next_y = 270
score_rect = pygame.Rect(320, score_y + 35, 170, 60)
level_rect = pygame.Rect(320, level_y + 35, 170, 60)
next_rect = pygame.Rect(320, next_y + 35, 170, 180)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
        if event.type == game.GAME_UPDATE and not game.game_over:
            game.move_down()

    # Drawing

    screen.fill(DARK_BLUE)
    score_value_surface = title_font.render(str(game.score), True, WHITE)
    screen.blit(score_surface, (365, score_y, 50, 50))
    level_value_surface = title_font.render(str(game.level), True, WHITE)
    screen.blit(level_surface, (365, level_y, 50, 50))
    screen.blit(next_surface, (375, next_y, 50, 50))

    if game.game_over:
        screen.blit(gameover_surface, (320, 500, 50, 50))

    # Score
    pygame.draw.rect(screen, LIGHT_BLUE, score_rect, 0, 10)
    screen.blit(
        score_value_surface,
        score_value_surface.get_rect(
            centerx=score_rect.centerx, centery=score_rect.centery
        ),
    )

    # Level
    pygame.draw.rect(screen, LIGHT_BLUE, level_rect, 0, 10)
    screen.blit(
        level_value_surface,
        level_value_surface.get_rect(
            centerx=level_rect.centerx, centery=level_rect.centery
        ),
    )

    # Next
    pygame.draw.rect(screen, LIGHT_BLUE, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
