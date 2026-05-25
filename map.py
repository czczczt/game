import pygame

class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # инициализацирует innit базового класса

        map_img = pygame.image.load('assets/map/backgr.png').convert()
        self.image = pygame.transform.scale(map_img, (800, 600))
        self.rect = self.image.get_rect()