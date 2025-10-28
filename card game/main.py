import arcade

screen_width = 800
screen_height = 600
screen_title = "Stage 2 Example"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, screen_title)
        arcade.set_background_color(arcade.color.MAHOGANY)
        self.x = 100
        self.y = 100
        self.speed_x = 0
        self.speed_y = 0
    
    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.x,self.y,20,arcade.color.RED)

    def on_update(self, delta_time):
        self.x += self.speed_x
        self.y += self.speed_y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.speed_x += 10
        if key == arcade.key.LEFT:
            self.speed_x -= 10
        if key == arcade.key.UP:
            self.speed_y += 10
        if key == arcade.key.DOWN:
            self.speed_y -= 10

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.speed_x = 0
        elif key in [arcade.key.DOWN, arcade.key.UP]:
            self.speed_y = 0

def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()