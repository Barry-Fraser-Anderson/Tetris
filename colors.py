class Colors:
    # 0     cell background
    # 1-7   blocks
    colors = [
        (26, 31, 40),
        (0, 255, 255),
        (0, 0, 255),
        (255, 128, 0),
        (255, 255, 0),
        (0, 255, 0),
        (128, 0, 128),
        (255, 0, 0),
    ]

    @classmethod
    def get_cell_colors(cls):
        return cls.colors
