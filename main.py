#!/usr/bin/env python3

#TODO 
#FEATURES
#Add animation 
#Game server needs to detect if a player disconnected
#Load levels dynamically, rather than hardcode level data in main.py
#Load all animations only once, not when player is created


import argparse

from game.game import Game

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Game client arguments')
    parser.add_argument('--name', type=str, default="default_name", required=True)
    args = parser.parse_args()
    game = Game(args.name)
    value = game.start_game()