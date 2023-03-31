import random
import arcade



class Spaceship(arcade.Sprite):
    def __init__(self, game, name):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = game.width // 2
        self.center_y =  80
        self.width = 70
        self.height = 60
        self.name = name
        self.speed = 8
    


class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, w)
        self.center_y = h + 35
        self.angle = 180
        self.width = 70
        self.height = 60
        self.speed = 4


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=800, title="Interstellar Game2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self, "rezvane") 
        self.enemy = Enemy(self.width, self.height)


    #نمایش
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1000, 800, self.background)
        self.me.draw()
        self.enemy.draw()


    def on_key_press(self, symbol: int, modifiers: int): 
        if symbol ==arcade.key.A or symbol== arcade.key.LEFT:
            self.me.center_x = self.me.center_x - self.me.speed
        elif symbol ==arcade.key.D or symbol == arcade.key.RIGHT:
            self.me.center_x = self.me.center_x + self.me.speed
        elif symbol == arcade.key.SPACE:
            ...


    #تابعی که بصورت اتوماتیک سریع اجرا میشه
    def on_update(self, delta_time: float):
        self.enemy.center_y -= self.enemy.speed

 
window = Game()
arcade.run()