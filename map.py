# map.py
import pygame

class Map:
    def __init__(self):
        self.walls = pygame.sprite.Group()
        design = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]

        size = 8
        block_size = 40

        for y, row in enumerate(design):
            for x, cell in enumerate(row):
                if cell == 1:
                    wall = pygame.sprite.Sprite()
                    wall.image = pygame.Surface((block_size, block_size))
                    wall.image.set_colorkey((0, 0, 0))

                    for iy, irow in enumerate(design):
                        for ix, icell in enumerate(irow):
                            if icell == 1:
                                pygame.draw.rect(wall.image, (255, 255, 255), (ix * size, iy * size, size, size))

                    wall.rect = wall.image.get_rect()
                    wall.rect.x = x * block_size
                    wall.rect.y = y * block_size
                    self.walls.add(wall)

    def check_collision(self, player_rect):
        return pygame.sprite.spritecollideany(player_rect, self.walls)