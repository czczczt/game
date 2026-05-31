import pygame
from map import Map

class Menu(Map):
    def __init__(self):
        super().__init__()

        self.btn_frames = [pygame.image.load(f'assets/button/singleplayer{i}.png') for i in range(1, 13)]
        self.btn_frame = 0
        self.btn_count = 0
        self.btn_speed = 0.075
        self.btn_rect = self.btn_frames[0].get_rect(center=(self.WINDOW_SIZE[0]//2, self.WINDOW_SIZE[1]//2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.btn_rect.collidepoint(event.pos):
                return "start"
        return None

    def update(self, scaled_delta_time):
        super().update(scaled_delta_time)
        self.btn_count += scaled_delta_time
        if self.btn_count >= self.btn_speed:
            self.btn_count = 0
            self.btn_frame = (self.btn_frame + 1) % len(self.btn_frames)
        self.image.blit(self.btn_frames[self.btn_frame], self.btn_rect)

    def draw(self, screen):
        screen.blit(self.image, (0, 0))