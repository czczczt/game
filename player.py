import pygame
from setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # инициализацирует innit базового класса

        self.SIZE = SIZE # из настроек
        self.SPEED = SPEED
        self.ANIMATION_SPEED = ANIMATION_SPEED

        self.frame = 0 # для анимации
        self.count = 0 # для анимации
        #self.color = random.randint(1, 7)
        self.color = 1

        sprites = [pygame.image.load(f'assets/player/run/{i}.png') for i in range(1, 8)]
        base = sprites[self.color]
        w, h = base.get_size()
        # Попробуем корректно разделить спрайт-лист на 4 кадра адаптивно по ширине
        if w >= 4:
            frame_w = w // 4
            self.player_run = [base.subsurface(pygame.Rect(i * frame_w, 0, frame_w, h)).copy() for i in range(4)]
        else:
            # Непредвиденный формат изображения — используем один и тот же кадр несколько раз
            self.player_run = [base.copy() for _ in range(4)]
        self.image = base.copy()
        self.rect = self.image.get_rect() # отрисовка персонажа
        self.rect.center = (200, 960) # корды спавна персонажа

    def animation(self, frames, scaled_delta_time):
        self.count += scaled_delta_time
        if self.count >= self.ANIMATION_SPEED: # смена кадра зависит от ANIMATION_SPEED
            self.count = 0
            self.frame += 1
            if self.frame == len(frames):
                self.frame = 0
        if self.frame >= len(frames):
            self.frame = 0
        self.image = pygame.transform.scale(frames[self.frame], self.SIZE) # отрисовка фрейма анимации

    def update(self, scaled_delta_time):
        keys = pygame.key.get_pressed()
        speed = self.SPEED * scaled_delta_time * 60 # лок на 60 фпс, чтобы на всех пк скорость была одинаковой

        if keys[pygame.K_a] and self.rect.x > -200 and not keys[pygame.K_d]: # AD движение
            self.rect.x -= speed
            self.animation(self.player_run, scaled_delta_time)
        elif keys[pygame.K_d] and self.rect.x < 1480 and not keys[pygame.K_a]:
            self.rect.x += speed
            self.animation(self.player_run, scaled_delta_time)

        else:
            self.image = pygame.transform.scale(self.player_run[0], self.SIZE)