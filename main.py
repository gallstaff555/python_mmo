#!/usr/bin/env python3

import asyncio
import socketio
import time
from game.game import start_game

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("connection established")

@sio.event
async def disconnect():
    print("disconnected from server")


async def main():
    print(f"Client starting...")
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
    print("asdf")
    time.sleep(5000)
    game = start_game()