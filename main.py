#!/usr/bin/env python3 

import pygame 
from config.config import Config
from world.tiled_map import TiledMap
from actors.player import Player
from actors.sprite_group import SpriteGroup
import os,sys 

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

cfg = Config()
map_file = resource_path("assets/forest_1.tmx")

pygame.init()
screen = pygame.display.set_mode((cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT / 2), pygame.RESIZABLE)

camera_sprite_group = SpriteGroup()
player = Player(cfg.PLAYER_START, camera_sprite_group, cfg.DEFAULT_ELF_ANIMATION_PATH, cfg.DEFAULT_ELF_ANIMATIONS)


clock = pygame.time.Clock()
running = True 

tile_map = TiledMap(f'{map_file}')

while running: 

    tile_map.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
            sys.exit()

    camera_sprite_group.update()
    camera_sprite_group.draw(screen)

    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()
