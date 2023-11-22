#!/usr/bin/env python3

#TODO 
#FEATURES
#Load levels dynamically, rather than hardcode level data in main.py
#Server should store player movement and broadcast to other players

#BUGS
#Fix movmenent speed: diagonally is faster than moving up/down

from game.game import Game

import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

game = Game(sio)

async def main():
    await sio.connect('http://localhost:5050')
    await game.start_game()
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())

    #asyncio.run(game.start_game())
    #game.start_game()