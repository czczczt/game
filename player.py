import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, settings):
        super().__init__() # инициализацирует innit базового класса

        self.SIZE = settings.SIZE # из настроек
        self.SPEED = settings.SPEED
        self.ANIMATION_SPEED = settings.ANIMATION_SPEED

        self.frame = 0 # для анимации
        self.count = 0
        self.jump = False # для движения
        self.jump_speed = 0
        self.fall = False
        self.fall_speed = 0

        sprite_player = pygame.image.load('assets/player/player.png') # загрузка всех спрайтов персонажа
        sprite_run = pygame.image.load('assets/player/run.png')
        sprite_jump = pygame.image.load('assets/player/jump.png')
        sprite_fall = pygame.image.load('assets/player/fall.png')
        sprite_attack1 = pygame.image.load('assets/player/attack1.png')
        sprite_attack2 = pygame.image.load('assets/player/attack2.png')

        self.run_right = [sprite_run.subsurface(pygame.Rect(i * 200, 0, 200, 200)) for i in range(8)] # массив фреймов
        self.run_left = []
        for i in range(8):
            frame = sprite_run.subsurface(pygame.Rect(i * 200, 0, 200, 200))
            frame_l = pygame.transform.flip(frame, True, False)
            self.run_left.append(frame_l)
        self.player = [sprite_player.subsurface(pygame.Rect(i * 200, 0, 200, 200)) for i in range(4)]
        self.jump = [sprite_jump.subsurface(pygame.Rect(i * 200, 0, 200, 200)) for i in range(2)]
        self.fall = [sprite_fall.subsurface(pygame.Rect(i * 200, 0, 200, 200)) for i in range(2)]
        self.attack1 = [sprite_attack1.subsurface(pygame.Rect(i * 200, 0, 200, 200)) for i in range(4)]
        self.attack2 = [sprite_attack2.subsurface(pygame.Rect(i * 200, 0, 200, 200)) for i in range(4)]

        # персонаж стоит
        w = sprite_player.subsurface(pygame.Rect(0, 0, 200, 200)) # обрезка спрайта
        self.image = pygame.transform.scale(w, (600, 600)) # размеры обрезки
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

        if keys[pygame.K_w] and self.rect.y > -200:
            self.rect.y -= speed
            frames = self.jump
            self.animation(frames, scaled_delta_time)
        elif keys[pygame.K_s] and self.rect.y < 660:
            self.rect.y += speed
            frames = self.fall
            self.animation(frames, scaled_delta_time)
        elif keys[pygame.K_a] and self.rect.x > -200:
            self.rect.x -= speed
            frames = self.run_left
            self.animation(frames, scaled_delta_time)
        elif keys[pygame.K_d] and self.rect.x < 1480:
            self.rect.x += speed
            frames = self.run_right
            self.animation(frames, scaled_delta_time)













