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
		#self.image = pygame.image.load(image).convert_alpha()
        self.player_frames = []
        self.FrameGenerator = AnimationFrameGenerator()
        self.idle_frames = self.FrameGenerator.get_frames(animation_path, animation_dict, "idle")
        self.player_frames = self.idle_frames
        # for i in range(0, 6):
        #     frame_file = resource_path(f"../assets/elf_pack/sword/elf_sword_color_3/idle/idle_{i}.png")
        #     frame = pygame.image.load(frame_file).convert_alpha()
        #     self.player_frames.append(frame)

        self.index = 0
        self.image = self.player_frames[0]
        self.rect = self.image.get_rect(center = pos)
        #self.rect = self.image.get_rect(topleft=(x,y))
        self.animation_time = cfg.PLAYER_ANIMATION_TIMER
        self.current_time = 0

    def update(self):
        self.index += 1
        if self.index >= len(self.player_frames):
            self.index = 0
        self.image = self.player_frames[self.index]




    # def load_images():
    #     player_frames = []
    #     for i in range(1, 6):
    #         frame_file = resource_path(f"../assets/elf_pack/archer/{i}.png")
    #         frame = pygame.image.load(frame_file)
    #         player_frames.append(frame)


