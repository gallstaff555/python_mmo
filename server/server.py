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
            #print(f"decoded data: {decoded_data}")
            payload = json.loads(decoded_data)
            header = payload['header']
            if header is None:
                print("Error: no header provided.")
            elif header == "update":
                self.handle_update(payload)
            elif header == "disconnect":
                self.handle_disconnect(payload)
            elif header == "connect":
                self.handle_connection(payload)
            else:
                print("Error with message occurred.")
            result_string = json.dumps(self.server.players)
            self.request.sendall(result_string.encode('utf-8'))

    def handle_connection(self, payload):
        player_name = f"{payload['name']}"
        if not player_name in self.server.players:
            print(f"Player {player_name} connected for first time.")
        self.server.players[player_name] = payload
        print(f"{player_name} connected!")

    def handle_disconnect(self, payload):
        player_name = f"{payload['name']}"
        print(f"Player {player_name} wants to disconnect...")
        if player_name in self.server.players:
            del self.server.players[player_name]
            print(f"{player_name} disconnected!")
        else:
            print(f"Could not find {player_name} in list of players.")
        print(f"Remaining player count: {len(self.server.players)}")

    def handle_update(self, payload):
        player_name = f"{payload['name']}"
        self.server.players[player_name] = payload
        #print(f"Player data: {self.server.players}, number of players: {len(self.server.players)}")

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 5000
    players = {}

    with GameServer((HOST, PORT), TCPHandler, players) as server:
        print(f"Server running on {HOST}:{PORT}")
        server.serve_forever()

