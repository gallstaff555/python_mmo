#!/usr/bin/env python3 

import pygame, pytmx, pyscroll
from game.config.config import Config
from game.actors.player import Player
import os,sys,time,random
import threading
import concurrent.futures

cfg = Config()

class Game():
    def __init__(self):

        self.result = [-1]

        pygame.init()
        self.screen = pygame.display.set_mode((cfg.SCREEN_WIDTH * cfg.CAMERA_SCALE, cfg.SCREEN_HEIGHT * cfg.CAMERA_SCALE), pygame.RESIZABLE)
        self.surface = pygame.Surface((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT)).convert()
        pygame.display.set_caption("Test MMO")

        #set up map and pyscroll
        self.map_file = self.resource_path("assets/forest_1.tmx")
        self.tmx_data = pytmx.load_pygame(self.map_file)
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.my_map_layer = pyscroll.BufferedRenderer(self.map_data, (cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT), clamp_camera=True)
        self.camera_group = pyscroll.PyscrollGroup(map_layer=self.my_map_layer, default_layer=cfg.DEFAULT_PLAYER_LAYER)

        #set up player and add to camera_group
        self.player = Player(cfg.PLAYER_START, cfg.DEFAULT_ELF_ANIMATION_PATH, cfg.DEFAULT_ELF_ANIMATIONS)
        self.camera_group.add(self.player)

        # set up invisible collision sprites
        self.collision_group = pygame.sprite.Group()
        self.object_layer = self.tmx_data.get_layer_by_name("Collision")
        for obj in self.object_layer:
            sprite_image = pygame.Surface((5, 5))  
            sprite_image.fill(pygame.Color('blue')) 
            sprite_mask = pygame.mask.from_surface(sprite_image) 
            sprite = pygame.sprite.Sprite() 
            sprite.image = sprite_image
            sprite.rect = sprite.image.get_rect(center = (obj.x, obj.y))
            sprite.mask = sprite_mask
            
            self.collision_group.add(sprite)

        #pygame set up
        self.clock = pygame.time.Clock()
        self.scale = pygame.transform.scale
        self.running = True 

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def update_server(self, data):
        time.sleep(.5)
        print(f"Sending player pos to server: {data}")
        latest = random.randint(1,100)
        self.result[0] = latest
        

    def start_game(self):

            result = 0
        #stop_thread = threading.Event()
        # with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        #     future = executor.submit(self.update_server, (self.player.rect.x, self.player.rect.y))

            while self.running: 

                pygame.time.Clock().tick(cfg.FPS)

                if (threading.active_count() < 2):
                    thread = threading.Thread(target=self.update_server, args=((self.player.rect.x, self.player.rect.y),))
                    thread.start()
                    print(self.result)


                # Player should face the mouse pointer
                mouse_x, mouse_y = pygame.mouse.get_pos()
                cam_x, cam_y = self.my_map_layer.view_rect.topleft
                if mouse_x / cfg.CAMERA_SCALE + cam_x < self.player.rect.center[0]:
                    self.player.flipped = True 
                else:
                    self.player.flipped = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        # stop_thread.set()
                        # thread.join()
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if cfg.MOVEMENT_TYPE == "mouse":
                            #calculate player true position with camera and camera scale offset 
                            world_x, world_y = mouse_x / cfg.CAMERA_SCALE + cam_x, mouse_y / cfg.CAMERA_SCALE + cam_y
                            self.player.move_to = (round(world_x), round(world_y))

                self.camera_group.update(self.collision_group)
                self.camera_group.center((self.player.rect.center))
                self.camera_group.draw(self.surface)

                # if cfg.TEST:
                #     self.image_border = self.player.animate_player.player_frames[0].copy()
                #     pygame.draw.rect(self.surface, (255,0,0), self.player.rect, 4)

                self.scale(self.surface, self.screen.get_size(), self.screen)
                pygame.display.flip()

            # stop_thread.set()
            # thread.join()
            pygame.quit()
            sys.exit()