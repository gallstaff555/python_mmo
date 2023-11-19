import pygame
from game.actors.animation_frame_generator import AnimationFrameGenerator
from game.config.config import Config


cfg = Config()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, animation_path, animation_dict, tmx_data):
        super().__init__()
        self.pos = pos
        self.move_to = None
        self.animations_map = self.load_animations(animation_path, animation_dict)
        self.player_frames = self.animations_map["idle"]
        self.speed = 3
        self.index = 0
        self.image = self.player_frames[0]
        self.rect = self.image.get_rect(center = self.pos)
        self.animation_time = cfg.PLAYER_ANIMATION_TIMER
        self.last_update = pygame.time.get_ticks()
        self.flipped = False
        self.tmx_data = tmx_data

    def load_animations(self, animation_path, animation_dict):
        FrameGenerator = AnimationFrameGenerator()
        animations_map = {}
        for anim in cfg.DEFAULT_ANIMATIONS_LIST:
            animations_map[anim] = FrameGenerator.get_frames(animation_path, animation_dict, anim, "regular")
            animations_map[f"{anim}_flipped"] = FrameGenerator.get_frames(animation_path, animation_dict, anim, "flipped")
        return animations_map

    def animate_self(self):
        if not self.move_to:
            if not self.flipped:
                self.player_frames = self.animations_map["idle"]
            else: 
                self.player_frames = self.animations_map["idle_flipped"]
        elif self.move_to:
            if self.move_to[0] < self.pos[0]:
                self.player_frames = self.animations_map["walk_flipped"]  
            else:
                self.player_frames = self.animations_map["walk"]

        now = pygame.time.get_ticks()
        if now - self.last_update > cfg.PLAYER_ANIMATION_TIMER:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.player_frames):
                self.index = 0
            self.image = self.player_frames[self.index]

    def update(self):
        self.animate_self()