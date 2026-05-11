import pygame
import sys
from player import Player

class Game:
    def __init__(self):
        self.is_paused = False
        self.game_speed = 1.0
        self.delta_time = 0.016

        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def set_game_speed(self, speed):
        self.game_speed = speed

    def update(self):
        if not self.is_paused:
            scaled_delta_time = self.delta_time * self.game_speed
            self.update_game_world(scaled_delta_time)
        else:
            self.update_paused_state()

    def update_game_world(self, scaled_delta_time):
        self.all_sprites.update()
        # All game logic here, such as moving objects, checking collisions, etc.
        # Example:
        # self.player.update(scaled_delta_time)
        # self.enemy.update(scaled_delta_time)
        # Physics.update(scaled_delta_time)
        pass

    def update_paused_state(self):
        # Update game menu or other paused state interactions
        # Example:
        # menu.update()
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.all_sprites.draw(screen)
        # All rendering here
        # Example:
        # self.player.draw(screen)
        # self.enemy.draw(screen)
        # self.ui.draw(screen)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    game = Game()

    running = True

    # classic game loop: Input -> Update -> Render
    while running:
        # 1. Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game.toggle_pause()

        # 2. Update
        game.update()

        # 3. Render
        game.draw(screen)
        pygame.display.flip()

        game.delta_time = clock.tick(60) / 1000.0  # seconds since last frame

    pygame.quit()
    sys.exit()