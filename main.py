#!/usr/bin/env python3

#TODO 
#FEATURES
#Add collision detection and prevent player from moving further if collision detected
#Add marker to map after clicking to move 
#Server should store player movement and broadcast to other players

#BUGS
#Fix movmenent speed: diagonally is faster than moving up/down

from game.game import Game

if __name__ == '__main__':
    game = Game()
    game.start_game()