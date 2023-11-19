import pygame,math
from game.config.config import Config

cfg = Config()

class MovePlayer():
    def __init__(self, player, collision_group):
        self.player = player 
        self.collision_group = collision_group
    
    def set_move_to_location(self, location):
        self.player.move_to = location
        print(f"Moving player to {location}")

    def move_by_coordinates(self):
        dx = self.player.move_to[0] - self.player.pos[0]
        dy = self.player.move_to[1] - self.player.pos[1]
        distance = math.sqrt(dx**2 + dy**2)

        if distance > self.player.speed:
            if self.check_collision():
                print("Collision!")
            temp_x = self.player.pos[0] + dx / distance * self.player.speed
            temp_y = self.player.pos[1] + dy / distance * self.player.speed
            self.player.pos = (temp_x, temp_y)
            self.player.rect.center = (temp_x, temp_y)
        else:
            if self.check_collision():
                print("Collision!")
            temp_x = self.player.move_to[0]
            temp_y = self.player.move_to[1]
            self.player.pos = (temp_x, temp_y)
            self.player.rect.center = (temp_x, temp_y)
            return True
        return False
    
    def check_collision(self):
        collisions = pygame.sprite.spritecollide(self.player, self.collision_group, False)
        for collided_sprite in collisions:
            return True

    def update(self):
        self.keyboard_input()
        # if self.player.move_to:
        #     if self.move_by_coordinates():
        #         self.player.move_to = None  

    def keyboard_input(self):

        keys = pygame.key.get_pressed()

        if not keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            if self.player.flipped:
                self.player.player_frames = self.player.animations_map["idle_flipped"]
            else:
                self.player.player_frames = self.player.animations_map["idle"]

        if keys[pygame.K_UP] and self.player.rect.y > -20:
            self.player.direction.y = -1
            if self.player.flipped:
                self.player.player_frames = self.player.animations_map["walk_flipped"]
            else:
                self.player.player_frames = self.player.animations_map["walk"]
        elif keys[pygame.K_DOWN] and self.rect.y < cfg.DEFAULT_LEVEL_SIZE * 1.5 - 55:
            self.player.direction.y = 1
            if self.player.flipped:
                self.player.player_frames = self.player.animations_map["walk_flipped"]
            else:
                self.player.player_frames = self.player.animations_map["walk"]
        else:
            self.player.direction.y = 0

        if keys[pygame.K_RIGHT] and self.player.rect.x < cfg.DEFAULT_LEVEL_SIZE * 1.5 - 40:
            self.player.direction.x = 1
            self.player.player_frames = self.player.animations_map["walk"]
            self.player.flipped = False
        elif keys[pygame.K_LEFT] and self.player.rect.x > -20:
            self.player.direction.x = -1
            self.player.flipped = True
            self.player.player_frames = self.player.animations_map["walk_flipped"]
        else:
            self.player.direction.x = 0  