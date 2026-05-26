import pygame
import sys
from player import Player
from map import Map

class Map_settings:
    def __init__(self):
        self.WINDOW_SIZE = (1920, 1080) # размер экрана
        self.BACKGROUND_SPEED = 0.5 # скорость анимации фона

class Player_settings:
    def __init__(self):
        self.SPEED = 10 # скорость персонажа
        self.SIZE = (610, 610) # размер персонажа
        self.ANIMATION_SPEED = 0.1 # скорость анимации
        self.JUMP_COUNT = 14 # высота прыжка


class Game:
    def __init__(self):
        self.is_paused = False
        self.game_speed = 1.0
        self.delta_time = 0.016 # время для 60 фпс

        self.all_sprites = pygame.sprite.Group()
        self.player = Player(Player_settings()) # инициализация классов
        self.map = Map(Map_settings())
        self.all_sprites.add(self.map, self.player)

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def set_game_speed(self, speed):
        self.game_speed = speed

    def update(self):
        if not self.is_paused:
            scaled_delta_time = self.delta_time * self.game_speed # реальное время между кадрами * коэф
            self.update_game_world(scaled_delta_time)
        else:
            self.update_paused_state()

    def update_game_world(self, scaled_delta_time):
        self.player.update(scaled_delta_time) # передача реального времени между кадрами
        self.map.update()

    def update_paused_state(self):
        # Update game menu or other paused state interactions
        # Example:
        # menu.update()
        pass

    def draw(self, screen):
        self.all_sprites.draw(screen) # отрисовка всех классов сразу
        screen.blit(text_start, (200, 200)) # отрисовка текста в координатах (200, 200)


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(Map_settings().WINDOW_SIZE) # открытие окна с размерами WINDOW_SIZE из класса
    pygame.display.set_caption("100 БАЛЛОВ") # название
    icon = pygame.image.load('assets/logo.png') # иконка
    pygame.display.set_icon(icon)
    font1 = pygame.font.Font('assets/font/1.ttf', 30) # шрифт
    text_start = font1.render('начало', True, 'red')
    main_sound = pygame.mixer.Sound('assets/audio/main.mp3') # фоновая музыка
    #main_sound.play()


    clock = pygame.time.Clock()
    game = Game()

    running = True

    while running:
        for event in pygame.event.get(): # закрытие окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: # пауза на p
                if event.key == pygame.K_p:
                    game.toggle_pause()

        game.update()

        game.draw(screen)
        pygame.display.flip()

        game.delta_time = clock.tick(60) / 1000.0 # реальное время между кадрами в секундах

    pygame.quit()
    sys.exit()