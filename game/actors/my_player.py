from game.actors.base_player import BasePlayer
#from game.actors.base_player import BasePlayer
from game.actors.move_player import MovePlayer

class MyPlayer(BasePlayer):
    def __init__(self, name, player_class, race, start_pos, animation_path, animation_frames):
        super().__init__(name, player_class, race, start_pos, animation_path, animation_frames)
        self.move_player = MovePlayer()

    def update(self, collision_group):
        self.animate_player.animate(self)
        self.move_player.update(self, self.animate_player, collision_group)