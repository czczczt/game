import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # инициализацирует innit базового класса

        player_img = pygame.image.load('assets/entities/player.png').convert_alpha()
        self.image = pygame.transform.scale(player_img, (60, 60))

        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

        self.speed = 4

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed