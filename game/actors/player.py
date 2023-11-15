import pygame
from game.actors.animation_frame_generator import AnimationFrameGenerator
from game.config.config import Config
from pygame.math import Vector2
import math

cfg = Config()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, animation_path, animation_dict):
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

    def load_animations(self, animation_path, animation_dict):
        FrameGenerator = AnimationFrameGenerator()
        animations_map = {}
        for anim in cfg.DEFAULT_ANIMATIONS_LIST:
            animations_map[anim] = FrameGenerator.get_frames(animation_path, animation_dict, anim, "regular")
            animations_map[f"{anim}_flipped"] = FrameGenerator.get_frames(animation_path, animation_dict, anim, "flipped")
        return animations_map

    def set_move_to_location(self, location):
        self.move_to = location
        print(f"Moving to {self.move_to}")

    def move_by_coordinates(self):
        dx = self.move_to[0] - self.pos[0]
        dy = self.move_to[1] - self.pos[1]
        distance = math.sqrt(dx**2 + dy**2)

        if distance > self.speed:
            temp_x = self.pos[0] + dx / distance * self.speed
            temp_y = self.pos[1] + dy / distance * self.speed
            self.pos = (temp_x, temp_y)
            self.rect.center = (temp_x, temp_y)
        else:
            temp_x = self.move_to[0]
            temp_y = self.move_to[1]
            self.pos = (temp_x, temp_y)
            self.rect.center = (temp_x, temp_y)
            return True
        return False

    def animate_self(self):
        if not self.move_to:
            if not self.flipped:
                self.player_frames = self.animations_map["idle"]
            else: 
                self.player_frames = self.animations_map["idle_flipped"]
        elif self.move_to:
            if self.flipped:
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
        #self.keyboard_input()
        
        if self.move_to:
            if self.move_by_coordinates():
                self.move_to = None
        

    # def move_to(self):
    #     if not (self.pos == self.target_location):
    #         diff_vector = self.distance_between_vectors(self.target_location, self.pos)    
    #         #distance_x = distance[0] 
    #         #print(difference)
    #         movement_vector = diff_vector.normalize() * self.speed
    #         self.rect.center += self.direction * self.speed
    #         self.pos += diff_vector
    #         self.rect.center = self.pos

    # def distance_between_vectors(self, vector1, vector2):
    #     return vector1 - vector2

    # def keyboard_input(self):

    #     keys = pygame.key.get_pressed()

    #     if not keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
    #         if self.flip:
    #             self.player_frames = self.animations_map["idle_flipped"]
    #         else:
    #             self.player_frames = self.animations_map["idle"]

    #     if keys[pygame.K_UP] and self.rect.y > -20:
    #         self.direction.y = -1
    #         if self.flip:
    #             self.player_frames = self.animations_map["walk_flipped"]
    #         else:
    #             self.player_frames = self.animations_map["walk"]
    #     elif keys[pygame.K_DOWN] and self.rect.y < cfg.DEFAULT_LEVEL_SIZE * 1.5 - 55:
    #         self.direction.y = 1
    #         if self.flip:
    #             self.player_frames = self.animations_map["walk_flipped"]
    #         else:
    #             self.player_frames = self.animations_map["walk"]
    #     else:
    #         self.direction.y = 0

    #     if keys[pygame.K_RIGHT] and self.rect.x < cfg.DEFAULT_LEVEL_SIZE * 1.5 - 40:
    #         self.direction.x = 1
    #         self.player_frames = self.animations_map["walk"]
    #         self.flip = False
    #     elif keys[pygame.K_LEFT] and self.rect.x > -20:
    #         self.direction.x = -1
    #         self.flip = True
    #         self.player_frames = self.animations_map["walk_flipped"]
    #     else:
    #         self.direction.x = 0  