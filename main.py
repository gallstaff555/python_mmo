#!/usr/bin/env python3

#TODO 
#FEATURES
#Load levels dynamically, rather than hardcode level data in main.py
#Server should store player movement and broadcast to other players

#BUGS
#Fix movmenent speed: diagonally is faster than moving up/down

from game.game import Game

if __name__ == '__main__':
    game = Game()
    value = game.start_game()
    print(int(value))