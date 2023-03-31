import arcade

class Heart(arcade.Sprite):
    def __init__(self, x):
        super().__init__("E:\python home work\python-corse\python-corse\Assignment-14\heart.png")
        self.center_x = 30 * x
        self.center_y = 60
        self.width = 30
        self.height = 35