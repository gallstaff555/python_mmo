#!/usr/bin/env python3

import socketserver
import json

class GameServer(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        self.players = {}
        super().__init__(request, client_address, server)
        

    def handle(self):
        raw_data = self.request.recv(1024).strip()
        decoded_data = raw_data.decode("utf-8").replace("'", "\"")
        json_data = json.loads(decoded_data)
        player_name = f"{json_data['name']}"
        print(player_name)
        self.players[player_name] = json_data["pos"]
        result_string = json.dumps(self.players)

        #self.players[f"{player_id}"] = json_data
        #print(self.players)
        #print(f"{self.client_address[0]} wrote: {data}")
        self.request.sendall(result_string.encode('utf-8'))

if __name__ == "__main__":
    
    HOST, PORT = "localhost", 5000

    with socketserver.TCPServer((HOST, PORT), GameServer) as server:
        print(f"Server running on {HOST}:{PORT}")
        server.serve_forever()
