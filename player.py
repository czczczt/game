import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # инициализацирует innit базового класса

        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.speed = 4

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed