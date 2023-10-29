import pygame 
from game.actors.AnimationFrameGenerator import AnimationFrameGenerator
from game.config.config import Config

#TODO normalize speed when traveling diagonally

cfg = Config()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, animation_path, animation_dict):
        super().__init__()
        
        self.pos = pygame.Vector2(pos)
        self.animations_map = self.load_animations(animation_path, animation_dict)
        self.player_frames = self.animations_map["idle"]
        self.speed = 3
        self.direction = pygame.math.Vector2()
        self.index = 0
        self.image = self.player_frames[0]
        self.rect = self.image.get_rect(center = pos)
        self.animation_time = cfg.PLAYER_ANIMATION_TIMER
        self.last_update = pygame.time.get_ticks()
        self.flip = False
        self.moving = False

    def load_animations(self, animation_path, animation_dict):
        FrameGenerator = AnimationFrameGenerator()
        animations_map = {}
        for anim in cfg.DEFAULT_ANIMATIONS_LIST:
            animations_map[anim] = FrameGenerator.get_frames(animation_path, animation_dict, anim, "regular")
            animations_map[f"{anim}_flipped"] = FrameGenerator.get_frames(animation_path, animation_dict, anim, "flipped")
        return animations_map

    def input(self):

        keys = pygame.key.get_pressed()

        if not keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            if self.flip:
                self.player_frames = self.animations_map["idle_flipped"]
            else:
                self.player_frames = self.animations_map["idle"]

        if keys[pygame.K_UP] and self.rect.y > -20:
            self.direction.y = -1
            if self.flip:
                self.player_frames = self.animations_map["walk_flipped"]
            else:
                self.player_frames = self.animations_map["walk"]
        elif keys[pygame.K_DOWN] and self.rect.y < cfg.DEFAULT_LEVEL_SIZE * 1.5 - 55:
            self.direction.y = 1
            if self.flip:
                self.player_frames = self.animations_map["walk_flipped"]
            else:
                self.player_frames = self.animations_map["walk"]
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] and self.rect.x < cfg.DEFAULT_LEVEL_SIZE * 1.5 - 40:
            self.direction.x = 1
            self.player_frames = self.animations_map["walk"]
            self.flip = False
        elif keys[pygame.K_LEFT] and self.rect.x > -20:
            self.direction.x = -1
            self.flip = True
            self.player_frames = self.animations_map["walk_flipped"]
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


