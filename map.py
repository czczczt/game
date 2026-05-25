import pygame

class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # инициализацирует innit базового класса

        self.image = pygame.image.load('assets/map/background.png')
        self.rect = self.image.get_rect()