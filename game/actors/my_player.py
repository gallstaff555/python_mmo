from game.actors.BasePlayer import BasePlayer
from game.actors.move_player import MovePlayer

class MyPlayer(BasePlayer):
    def __init__(self, name, start_pos, appearance):
        super().__init__(name, start_pos, appearance)
        self.move_player = MovePlayer()

    def update(self, collision_group):
        self.animate_player.animate(self)
        self.move_player.update(self, self.animate_player, collision_group)