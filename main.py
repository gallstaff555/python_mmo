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
screen = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))

player = Player(cfg.PLAYER_START, cfg.DEFAULT_ELF_ANIMATION_PATH, cfg.DEFAULT_ELF_ANIMATIONS)
player_sprite_group = SpriteGroup(player)

clock = pygame.time.Clock()
running = True 

tile_map = TiledMap(f'{map_file}')

while running: 

    tile_map.render(screen)
    player_sprite_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
            sys.exit()

    player_sprite_group.update()
    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()
