import pygame 
import sys,os
from config.config import Config
from actors.AnimationFrameGenerator import AnimationFrameGenerator

cfg = Config()

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, animation_path, animation_dict):
        super().__init__()
        
        self.pos = pygame.Vector2(pos)
        self.FrameGenerator = AnimationFrameGenerator()
        self.idle_frames = self.FrameGenerator.get_frames(animation_path, animation_dict, "idle")
        self.player_frames = self.idle_frames
        self.speed = 8
        self.direction = pygame.math.Vector2()
        self.index = 0
        self.image = self.player_frames[0]
        self.rect = self.image.get_rect(center = pos)
        self.animation_time = cfg.PLAYER_ANIMATION_TIMER
        self.last_update = pygame.time.get_ticks()

    def input(self):

        print(self.rect.center)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.y > -20:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] and self.rect.y < cfg.DEFAULT_LEVEL_SIZE * 1.5 - 55:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] and self.rect.x < cfg.DEFAULT_LEVEL_SIZE * 1.5 - 40:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] and self.rect.x > -20:
            self.direction.x = -1
        else:
            self.direction.x = 0      

    def update(self):

        now = pygame.time.get_ticks()
        if now - self.last_update > cfg.PLAYER_ANIMATION_TIMER:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.player_frames):
                self.index = 0
            self.image = self.player_frames[self.index]

        self.input()
        self.rect.center += self.direction * self.speed

    def get_position(self):
        print(f"{self.rect.x}, {self.rect.y}")
        #return (self.rect.y, self.rect.x)



