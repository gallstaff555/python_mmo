import pygame
from game.config.config import Config
from game.actors.animate_player import AnimatePlayer
from game.actors.move_player import MovePlayer

cfg = Config()

class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos, animation_path, animation_dict):
        super().__init__()
        self.name = "Gallstaff"
        self.move_player = MovePlayer()
        self.animate_player = AnimatePlayer(animation_path, animation_dict)
        self.image = self.animate_player.player_frames[0]
        self.mask = self.animate_player.player_mask[0]
        self.rect = self.image.get_rect(center = start_pos)
        self.pos = start_pos
        self.move_to = None
        self.speed = cfg.SPEED
        self.flipped = False
        self.direction_x = 0
        self.direction_y = 0

    def update(self, collision_group):
        self.animate_player.animate(self)
        self.move_player.update(self, self.animate_player, collision_group)