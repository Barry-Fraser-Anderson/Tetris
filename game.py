import pygame
import random
from grid import Grid
from blocks import *

GRID_OFFSET = 10


class Game:
    def __init__(self):
        self.grid = Grid()
        self.reset()

        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")

        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 800
        self.score += move_down_points

    def get_random_block(self):
        id = random.randint(1, 7)
        match id:
            case 1:
                return IBlock()
            case 2:
                return JBlock()
            case 3:
                return LBlock()
            case 4:
                return OBlock()
            case 5:
                return SBlock()
            case 6:
                return TBlock()
            case 7:
                return ZBlock()

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
            self.total_rows_cleared += rows_cleared
        if not self.block_fits():
            self.game_over = True

    def reset(self):
        self.grid.reset()
        self.game_over = False
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.level = 1
        self.total_rows_cleared = 0

    def level_check(self):
        if self.total_rows_cleared >= self.level * 10:
            self.level += 1
            self.total_rows_cleared = 0

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.col):
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.col):
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, GRID_OFFSET + 1, GRID_OFFSET + 1)

        if self.next_block.id == 1:
            self.next_block.draw(screen, 255, 380)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 370)
        else:
            self.next_block.draw(screen, 270, 360)
