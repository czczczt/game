import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, SPEED):
        super().__init__() # инициализацирует innit базового класса

        sprite_player = pygame.image.load('assets/player/sprite_player.png')
        player = sprite_player.subsurface(pygame.Rect(0, 0, 200, 200)) # обрезка спрайта
        self.image = pygame.transform.scale(player, (600, 600)) # размеры обрезки

        self.rect = self.image.get_rect()
        self.rect.center = (100, 100) # корды спавна персонажа

        self.speed = SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed