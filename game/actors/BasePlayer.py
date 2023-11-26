import pygame
from game.config.config import Config
from game.actors.animate_player import AnimatePlayer

cfg = Config()

class BasePlayer(pygame.sprite.Sprite):
    def __init__(self, name, start_pos, appearance):
        super().__init__()
        self.name = name
        self.race = appearance["race"]
        self.animate_player = AnimatePlayer(appearance["path"], appearance["frames"])
        self.image = self.animate_player.player_frames[0]
        self.mask = self.animate_player.player_mask[0]
        self.rect = self.image.get_rect(center = start_pos)
        self.pos = start_pos
        self.move_to = None
        self.speed = cfg.SPEED
        self.flipped = False
        self.direction_x = 0
        self.direction_y = 0