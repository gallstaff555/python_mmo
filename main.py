#!/usr/bin/env python3

#TODO 
#FEATURES
#Load levels dynamically, rather than hardcode level data in main.py
#Server should store player movement and broadcast to other players

#BUGS
#Fix movmenent speed: diagonally is faster than moving up/down

import argparse

from game.game import Game

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Game client arguments')
    parser.add_argument('--id', type=int, default=1, required=True)
    args = parser.parse_args()
    game = Game(args.id)
    value = game.start_game()