#!/usr/bin/env python3 

import pygame 
from world.tiled_map import TiledMap
import os,sys 

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

map_file = resource_path("assets/forest_1.tmx")

pygame.init()
screen = pygame.display.set_mode((480, 320))

clock = pygame.time.Clock()
running = True 

tile_map = TiledMap(f'{map_file}')

while running: 

    tile_map.render(screen)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
