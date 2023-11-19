import pygame
from game.actors.animation_frame_generator import AnimationFrameGenerator
from game.config.config import Config

cfg = Config()

class AnimatePlayer():
    def __init__(self, animation_path, animation_dict):
        self.last_update = pygame.time.get_ticks()
        self.animation_map = self.load_animations(animation_path, animation_dict)

    def load_animations(self, animation_path, animation_dict):
            FrameGenerator = AnimationFrameGenerator()
            animations_map = {}
            for anim in cfg.DEFAULT_ANIMATIONS_LIST:
                animations_map[anim] = FrameGenerator.get_frames(animation_path, animation_dict, anim, "regular")
                animations_map[f"{anim}_flipped"] = FrameGenerator.get_frames(animation_path, animation_dict, anim, "flipped")
            return animations_map
    
    def get_animation(self, animation):
        return self.animation_map[animation]

    def animate(self, player):
        if player.movement_type == "mouse":
            if not player.move_to:
                if not player.flipped:
                    player.player_frames = self.animations_map["idle"]
                else: 
                    player.player_frames = self.animations_map["idle_flipped"]
            elif player.move_to:
                if player.move_to[0] < self.player.pos[0]:
                    player.player_frames = self.animations_map["walk_flipped"]  
                else:
                    player.player_frames = self.animations_map["walk"]
        elif player.movement_type == "keyboard":
            pass

        now = pygame.time.get_ticks()
        if now - player.last_update > cfg.PLAYER_ANIMATION_TIMER:
            player.last_update = now
            player.index += 1
            if player.index >= len(player.player_frames):
                player.index = 0
            player.image = player.player_frames[player.index]