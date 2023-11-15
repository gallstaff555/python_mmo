#!/usr/bin/env python3

import socket 
import _thread
import sys 

server = '127.0.0.1'
port = 5000
max_connections = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(max_connections)

def threaded_client(conn):
    conn.send(str.encode("Connected."))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
        
            if not data:
                print('Disconnected.')
                break
            else:
                print(f'Received: {reply}')
                print(f'Sending: {reply}')

            conn.sendall(str.encode(reply))
        except:
            break
    
    print('Closing connection.')
    conn.close()

while True:
    conn, addr = s.accept()
    print("connected to:", addr)

    _thread.start_new_thread(threaded_client, (conn,))