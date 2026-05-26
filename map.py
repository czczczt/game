import pygame

class Map(pygame.sprite.Sprite):
    def __init__(self, settings):
        super().__init__() # инициализацирует innit базового класса

        self.WINDOW_SIZE = settings.WINDOW_SIZE # из настроек
        self.BACKGROUND_SPEED = settings.BACKGROUND_SPEED

        self.bg_x = 0 # для анимации фона

        self.bg_load = pygame.image.load('assets/map/background.png')
        self.bg = pygame.transform.scale(self.bg_load, self.WINDOW_SIZE) # обрезка фона до размеров WINDOW_SIZE из настроек
        self.image = pygame.Surface(self.WINDOW_SIZE)
        self.rect = self.image.get_rect()

    def update(self):
        self.bg_x -= self.BACKGROUND_SPEED # два фона двигаются влево
        if self.bg_x <= -1920: # когда 1 полностью ушел за экран - перемещение в начало
            self.bg_x = 0
        self.image.blit(self.bg, (self.bg_x, 0))
        self.image.blit(self.bg, (self.bg_x + 1920, 0))