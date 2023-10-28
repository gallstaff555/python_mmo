import pygame 
import os,sys

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class AnimationFrameGenerator():

    def get_frames(self, path, anim_dict, type, orientation):
        frames = []
        for i in range(0, anim_dict[type]):
            frame_file = resource_path(f"{path}/{type}/{orientation}/{type}_{i}.png")
            frame = pygame.image.load(frame_file).convert_alpha()
            frames.append(frame)
        return frames
