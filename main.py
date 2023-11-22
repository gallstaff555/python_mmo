#!/usr/bin/env python3

#TODO 
#FEATURES
#Load levels dynamically, rather than hardcode level data in main.py
#Server should store player movement and broadcast to other players

#BUGS
#Fix movmenent speed: diagonally is faster than moving up/down

from game.game import Game


import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')
sio.wait()

if __name__ == '__main__':
    game = Game(sio)
    game.start_game()