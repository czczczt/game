import pygame
import sys
from menu import Menu
from player import Player
from map import Map


class Game:
    def __init__(self):
        self.is_paused = False
        self.game_speed = 1.0
        self.delta_time = 0.016 # время для 60 фпс
        self.state = "menu"

        self.menu = Menu()
        self.all_sprites = pygame.sprite.Group()
        self.player = Player() # инициализация классов
        self.map = Map()
        self.all_sprites.add(self.map, self.player) # порядок отрисовки

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def set_game_speed(self, speed):
        self.game_speed = speed

    def update(self):
        if self.state == "menu":
            scaled_delta_time = self.delta_time * self.game_speed # реальное время между кадрами * коэф
            self.menu.update(scaled_delta_time)
        elif not self.is_paused:
            scaled_delta_time = self.delta_time * self.game_speed
            self.update_game_world(scaled_delta_time)

    def update_game_world(self, scaled_delta_time):
        self.player.update(scaled_delta_time) # передача реального времени между кадрами
        self.map.update(scaled_delta_time)

    def update_paused_state(self):
        # Update game menu or other paused state interactions
        # Example:
        # menu.update()
        pass

    def draw(self, screen):
        if self.state == "menu":
            self.menu.draw(screen)
        else:
            self.all_sprites.draw(screen)

if __name__ == "__main__":
    pygame.init()
    game = Game()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(game.map.WINDOW_SIZE) # открытие окна с размерами WINDOW_SIZE
    pygame.display.set_caption("100 БАЛЛОВ") # название
    icon = pygame.image.load('assets/logo.png') # иконка
    pygame.display.set_icon(icon)
    font1 = pygame.font.Font('assets/font/ArcBlack.ttf', 30) # шрифт
    main_sound = pygame.mixer.Sound('assets/audio/main.mp3') # фоновая музыка
    #main_sound.play()

    running = True

    while running:
        for event in pygame.event.get(): # закрытие окна
            if event.type == pygame.QUIT:
                running = False
            if game.state == "menu":
                if game.menu.handle_event(event) == "start":
                    game.state = "playing"
            elif event.type == pygame.KEYDOWN: # пауза на p
                if event.key == pygame.K_p:
                    game.toggle_pause()

        game.update()

        game.draw(screen)
        pygame.display.flip()

        game.delta_time = clock.tick(60) / 1000.0 # реальное время между кадрами в секундах

    pygame.quit()
    sys.exit()