#!/usr/bin/env python3

import socketserver

class GameServer(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} wrote: {data}")
        self.request.sendall(data)

if __name__ == "__main__":
    
    HOST, PORT = "localhost", 5000

    with socketserver.TCPServer((HOST, PORT), GameServer) as server:
        print(f"Server running on {HOST}:{PORT}")
        server.serve_forever()
