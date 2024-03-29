import time
import arcade
from spaceship import Spaceship
from enemy import Enemy
from heart import Heart

    

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=800, title="Interstellar Game2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self.width, "rezvane") 
        self.Enemy_list = []
        self.heart_list = []
        self.score = 0
        self.game_over_background = arcade.load_texture("E:\python home work\python-corse\python-corse\Assignment-14\Game-Over.png")
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.game_over_sound = arcade.load_sound(":resources:sounds/gameover2.wav")
        self.state = "gaming"
        self.timeout = time.time()
        self.enemy_speed = 1.5
    

        for i in range(1, 4):
            heart = Heart(i)
            self.heart_list.append(heart)

        
    #نمایش
    def on_draw(self):
        arcade.start_render()

        if self.state == "gaming":
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
            self.me.draw()
            score_text = f"Score: {self.score}"
            arcade.draw_text(score_text, self.width -120 , 60, arcade.csscolor.WHEAT, 20)

            for enemy in self.Enemy_list:
                enemy.draw()

            for bullet in self.me.bullet_list:
                bullet.draw()

            for heart in self.heart_list:
                heart.draw()


        elif self.state == "Game Over":
            arcade.draw_lrwh_rectangle_textured(100, 200, 400, 400, self.game_over_background)

        arcade.finish_render()


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
        self.me.move()

        
        if time.time() > self.timeout + 3:
            new_enemy = Enemy(self.width, self.height, self.enemy_speed)
            self.Enemy_list.append(new_enemy)
            self.enemy_speed += 0.25
            self.timeout = time.time()

        for enemy in self.Enemy_list:
            enemy.move()
            if arcade.check_for_collision(self.me, enemy):
                self.state = "Game Over"
                self.on_draw() 
                arcade.play_sound(self.game_over_sound, 1, 0, False, 1)
                time.sleep(5)
                exit(0)

            if len(self.heart_list) > 0 :
                if enemy.center_y < 0 :
                    self.Enemy_list.remove(enemy)
                    self.heart_list.pop()
            else:
                self.state = "Game Over"
                self.on_draw()
                arcade.play_sound(self.game_over_sound, 1, 0, False, 1)
                time.sleep(5)
                exit(0)

        
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    arcade.play_sound(self.explosion_sound)
                    self.score += 1
                    self.Enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)

                if bullet.center_y > self.height:
                    self.me.bullet_list.remove(bullet)

        

        for bullet in self.me.bullet_list:
            bullet.move()


        #if random.randint(1, 100) == 6:
        #    self.new_enemy = Enemy(self.width, self.height)
        #    self.Enemy_list.append(self.new_enemy)

        
 
window = Game()
arcade.run()