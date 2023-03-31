import random
import arcade


class Enemy(arcade.Sprite):
    def __init__(self, w, h, enemy_speed):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, w)
        self.center_y = h + 35
        self.angle = 180
        self.width = 70
        self.height = 60
        self.speed = enemy_speed

    def move(self):
        self.center_y -= self.speed