import pygame
from game.actors.animation_frame_generator import AnimationFrameGenerator
from game.config.config import Config
from game.actors.animate_player import AnimatePlayer
from game.actors.move_player import MovePlayer


cfg = Config()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, animation_path, animation_dict, tmx_data):
        super().__init__()
        self.move_player = MovePlayer()
        self.animate_player = AnimatePlayer(animation_path, animation_dict)
        self.player_frames = self.animate_player.get_animation("idle")
        self.pos = pos
        self.move_to = None
        self.speed = 3
        self.index = 0
        self.image = self.player_frames[0]
        self.rect = self.image.get_rect(center = self.pos)
        self.animation_time = cfg.PLAYER_ANIMATION_TIMER
        self.last_update = pygame.time.get_ticks()
        self.flipped = False
        self.tmx_data = tmx_data
        self.direction_x = 0
        self.direction_y = 0
        #self.movement_type = "mouse"
        self.movement_type = "keyboard"

    def update(self):
        self.animate_player.animate(self)
        self.move_player.update(self, self.animate_player)