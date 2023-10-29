import pygame

class PlayerAction():
    def __init__(self, player):
        self.player = player

    def handle_input(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(f"{mouse_x}, {mouse_y}")
        self.player.update_position(mouse_x, mouse_y)
        

