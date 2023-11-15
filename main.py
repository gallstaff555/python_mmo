#!/usr/bin/env python3

#TODO 
#FEATURES
#Add marker to map after clicking to move 
#Server should store player movement and broadcast to other players

#BUGS
#Fix bug where player walks in front of all trees 
#Fix issue where camera scale breaks click to move location
#Check if moving diagonally is faster than moving up/down

from game.game import Game

if __name__ == '__main__':
    game = Game()
    game.start_game()