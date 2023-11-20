import pygame
from game.actors.animation_frame_generator import AnimationFrameGenerator
from game.config.config import Config

cfg = Config()

class AnimatePlayer():
    def __init__(self, animation_path, animation_dict):
        self.last_update = pygame.time.get_ticks()
        self.animation_map = self.load_animations(animation_path, animation_dict)
        self.player_frames = self.animation_map["idle"]
        self.index = 0
        self.last_update = pygame.time.get_ticks()

    def load_animations(self, animation_path, animation_dict):
            FrameGenerator = AnimationFrameGenerator()
            animations = {}
            for anim in cfg.DEFAULT_ANIMATIONS_LIST:
                animations[anim] = FrameGenerator.get_frames(animation_path, animation_dict, anim, "regular")
                animations[f"{anim}_flipped"] = FrameGenerator.get_frames(animation_path, animation_dict, anim, "flipped")
            return animations

    def animate(self, player):
        if cfg.MOVEMENT_TYPE == "mouse":
            if not player.move_to:
                if not player.flipped:
                    self.player_frames = self.animation_map["idle"]
                else: 
                    self.player_frames = self.animation_map["idle_flipped"]
            elif player.move_to:
                if player.move_to[0] < player.pos[0]:
                    self.player_frames = self.animation_map["walk_flipped"]  
                else:
                    self.player_frames = self.animation_map["walk"]
        elif cfg.MOVEMENT_TYPE == "keyboard":
            pass

        now = pygame.time.get_ticks()
        if now - self.last_update > cfg.PLAYER_ANIMATION_TIMER:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.player_frames):
                self.index = 0
            player.image = self.player_frames[self.index]