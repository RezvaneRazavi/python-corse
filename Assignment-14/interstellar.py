import random
import arcade
from spaceship import Spaceship

    


class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, w)
        self.center_y = h + 35
        self.angle = 180
        self.width = 70
        self.height = 60
        self.speed = 2

    def move(self):
        self.center_y -= self.speed



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=800, title="Interstellar Game2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self.width, "rezvane") 
        self.doshmans = []

        
    #نمایش
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        for doshman in self.doshmans:
            doshman.draw()

        for bullet in self.me.bullet_list:
            bullet.draw()

    def on_key_press(self, symbol: int, modifiers: int): 
        if symbol == arcade.key.A or symbol== arcade.key.LEFT:
            self.me.change_x = -1
        elif symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.me.change_x = 1
        elif symbol == arcade.key.DOWN:
            self.me.change_x = 0

        elif symbol == arcade.key.SPACE:
            self.me.fire()


    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0


    #تابعی که بصورت اتوماتیک سریع اجرا میشه
    def on_update(self, delta_time: float):

        for doshman in self.doshmans:
            if arcade.check_for_collision(self.me, doshman):
                print("Game Over")
                exit(0)

        self.me.move()

        for doshman in self.doshmans:
            doshman.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        if random.randint(1, 100) == 6:
            self.new_doshman = Enemy(self.width, self.height)
            self.doshmans.append(self.new_doshman)

        
 
window = Game()
arcade.run()