import pygame


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0] * self.num_cols for _ in range(self.num_rows)]
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end=" ")
            print()

    def get_cell_colors(self):
        colors = [
            (26, 31, 40),
            (47, 230, 23),
            (232, 18, 18),
            (226, 116, 17),
            (237, 234, 4),
            (166, 0, 247),
            (21, 204, 209),
            (13, 64, 216),
        ]

        return colors

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(
                    col * self.cell_size + 1,
                    row * self.cell_size + 1,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
