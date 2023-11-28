#!/usr/bin/env python3

import socketserver
import json

class GameServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, players):
        super().__init__(server_address, RequestHandlerClass)
        self.players = players # Store the custom parameter

# override default handler class so we can use custom parameters
# use self.server.arg1 to access server data field
class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        raw_data = self.request.recv(2048).strip()
        if not raw_data:
            print(f"Client {self.client_address} may have disconnected")
        else:
            decoded_data = raw_data.decode("utf-8").replace("'", "\"")
            json_data = json.loads(decoded_data)
            player_name = f"{json_data['name']}"
            if not player_name in self.server.players:
                print(f"Player {player_name} connected for first time.")
            #self.server.players[player_name] = json_data["pos"]
            self.server.players[player_name] = json_data
            result_string = json.dumps(self.server.players)
            print(f"Player data: {self.server.players}, number of players: {len(self.server.players)}")

            self.request.sendall(result_string.encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 5000
    players = {}

    with GameServer((HOST, PORT), TCPHandler, players) as server:
        print(f"Server running on {HOST}:{PORT}")
        server.serve_forever()

