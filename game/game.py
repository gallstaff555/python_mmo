#!/usr/bin/env python3 

import pygame, pytmx, pyscroll
from game.config.config import Config
from game.actors.player import Player
from game.input.player_action import PlayerAction
import os,sys 

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

cfg = Config()

class Game():
    pygame.init()
    screen = pygame.display.set_mode((cfg.SCREEN_WIDTH * 2, cfg.SCREEN_HEIGHT * 2), pygame.RESIZABLE)
    temp_surface = pygame.Surface((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT)).convert()
    pygame.display.set_caption("Test MMO")

    #set up map and pyscroll
    map_file = resource_path("assets/forest_1.tmx")
    tmx_data = pytmx.load_pygame(map_file)
    map_data = pyscroll.data.TiledMapData(tmx_data)
    my_map_layer = pyscroll.BufferedRenderer(map_data, (cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT), clamp_camera=True)
    camera_group = pyscroll.PyscrollGroup(map_layer=my_map_layer, default_layer=2)

    #set up player and add to camera_group
    player = Player(cfg.PLAYER_START, cfg.DEFAULT_ELF_ANIMATION_PATH, cfg.DEFAULT_ELF_ANIMATIONS)
    camera_group.add(player)
    player_action = PlayerAction(player)

    #pygame set up
    clock = pygame.time.Clock()
    fps = 30
    scale = pygame.transform.scale
    running = True 

    while running: 

        pygame.time.Clock().tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_action.handle_input()
        
        # buttons = pygame.mouse.get_pressed()
        # if buttons[0]:
        #     print(buttons)
        #     player_action.handle_input()
        
        camera_group.update()
        camera_group.center((player.rect.center))
        camera_group.draw(temp_surface)
        scale(temp_surface, screen.get_size(), screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()
