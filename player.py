import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, settings):
        super().__init__() # инициализацирует innit базового класса

        self.SIZE = settings.SIZE # из настроек
        self.SPEED = settings.SPEED
        self.ANIMATION_SPEED = settings.ANIMATION_SPEED
        self.JUMP_COUNT = settings.JUMP_COUNT

        self.frame = 0 # для анимации
        self.count = 0
        self.is_jump = False # для движения
        self.jump_count = self.JUMP_COUNT
        self.is_fall = False
        self.fall_count = 0

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

        if not self.is_jump: # прыжок
            if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.rect.y >= 660:
                self.is_jump = True
        else:
            if self.jump_count >= -7:
                if self.jump_count > 0:
                    self.rect.y -= self.JUMP_COUNT
                    self.animation(self.jump, scaled_delta_time)
                elif self.jump_count < 0:
                    self.rect.y += self.JUMP_COUNT
                    self.animation(self.fall, scaled_delta_time)
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = self.JUMP_COUNT
                self.rect.y = 660

        if keys[pygame.K_a] and self.rect.x > -200: # AD движение
            self.rect.x -= speed
            if not self.is_fall and not self.is_jump:
                self.animation(self.run_left, scaled_delta_time)
        elif keys[pygame.K_d] and self.rect.x < 1480:
            self.rect.x += speed
            if not self.is_fall and not self.is_jump:
                self.animation(self.run_right, scaled_delta_time)
        # elif keys[pygame.K_s] and self.rect.y < 660:
        #     self.rect.y += speed
        #     self.animation(self.fall, scaled_delta_time)
        elif not self.is_jump:
            self.animation(self.player, scaled_delta_time)











