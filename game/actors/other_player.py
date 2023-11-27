from game.actors.base_player import BasePlayer

class OtherPlayer(BasePlayer):
    def __init__(self, name, player_class, race, start_pos, animation_path, animation_frames):
        super().__init__(name, player_class, race, start_pos, animation_path, animation_frames)
        
    def update_pos(self, new_coords, flipped, moving):
        self.rect.x = new_coords[0]
        self.rect.y = new_coords[1]
        self.flipped = flipped
        self.moving = moving

    def update(self, unused):
        self.animate_player.animate_other_player(self)