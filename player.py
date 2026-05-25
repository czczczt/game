import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, SIZE, SPEED, ANIMATION_SPEED):
        super().__init__() # инициализацирует innit базового класса

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

        w = sprite_player.subsurface(pygame.Rect(0, 0, 200, 200)) # обрезка спрайта
        self.image = pygame.transform.scale(w, (600, 600)) # размеры обрезки

        self.rect = self.image.get_rect()
        self.rect.center = (100, 100) # корды спавна персонажа

        self.SIZE = SIZE
        self.SPEED = SPEED
        self.ANIMATION_SPEED = ANIMATION_SPEED
        self.frame = 0
        self.count = 0

    def animation(self, frames, scaled_delta_time):
        self.count += scaled_delta_time
        if self.count >= self.ANIMATION_SPEED: # смена кадра зависит от ANIMATION_SPEED
            self.count = 0
            self.frame += 1
            if self.frame == len(frames) - 1:
                self.frame = 0
        self.image = pygame.transform.scale(frames[self.frame], self.SIZE)

    def update(self, scaled_delta_time):
        keys = pygame.key.get_pressed()
        speed = self.SPEED * scaled_delta_time * 60 # лок на 60 фпс, чтобы на всех пк скорость была одинаковой

        if keys[pygame.K_w]: self.rect.y -= speed
        if keys[pygame.K_s]: self.rect.y += speed
        if keys[pygame.K_a]:
            self.rect.x -= speed
            frames = self.run_left
            self.animation(frames, scaled_delta_time)
        if keys[pygame.K_d]:
            self.rect.x += speed
            frames = self.run_right
            self.animation(frames, scaled_delta_time)













