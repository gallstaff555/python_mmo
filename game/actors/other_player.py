from game.actors.base_player import BasePlayer

class OtherPlayer(BasePlayer):
    def __init__(self, name, start_pos, appearance):
        super().__init__(name, start_pos, appearance)
        
    def update_pos(self, new_coords, flipped, moving):
        self.rect.x = new_coords[0]
        self.rect.y = new_coords[1]
        self.flipped = flipped
        self.moving = moving

    def update(self, unused):
        self.animate_player.animate_other_player(self)