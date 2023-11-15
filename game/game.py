#!/usr/bin/env python3 

import pygame, pytmx, pyscroll
from game.config.config import Config
from game.actors.player import Player
import os,sys,math

cfg = Config()

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((cfg.SCREEN_WIDTH * 2, cfg.SCREEN_HEIGHT * 2), pygame.RESIZABLE)
        self.temp_surface = pygame.Surface((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT)).convert()
        pygame.display.set_caption("Test MMO")

        #set up map and pyscroll
        self.map_file = self.resource_path("assets/forest_1.tmx")
        self.tmx_data = pytmx.load_pygame(self.map_file)
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.my_map_layer = pyscroll.BufferedRenderer(self.map_data, (cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT), clamp_camera=True)
        self.camera_group = pyscroll.PyscrollGroup(map_layer=self.my_map_layer, default_layer=2)

        #set up player and add to camera_group
        self.player = Player(cfg.PLAYER_START, cfg.DEFAULT_ELF_ANIMATION_PATH, cfg.DEFAULT_ELF_ANIMATIONS)
        self.camera_group.add(self.player)

        #pygame set up
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.scale = pygame.transform.scale
        self.running = True 
        #print(dir(self.tmx_data))

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


    def start_game(self):

        while self.running: 

            pygame.time.Clock().tick(self.fps)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x / cfg.CAMERA_SCALE < self.player.rect.center[0]:
                self.player.flipped = True 
            else:
                self.player.flipped = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # calculate player true position with camera and camera scale offset 
                    cam_x, cam_y = self.my_map_layer.view_rect.topleft
                    world_x, world_y = mouse_x / cfg.CAMERA_SCALE + cam_x, mouse_y / cfg.CAMERA_SCALE + cam_y
                    self.player.set_move_to_location((round(world_x), round(world_y)))

            self.camera_group.update()
            self.camera_group.center((self.player.rect.center))
            self.camera_group.draw(self.temp_surface)
            self.scale(self.temp_surface, self.screen.get_size(), self.screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()
