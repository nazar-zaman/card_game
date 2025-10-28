import arcade

screen_width = 800
screen_height = 600
screen_title = "Stage 2 Example"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, screen_title)
        arcade.set_background_color(arcade.color.WHITE)
        
        self.x = 100
        self.y = 100
        self.circle_r = 40
        self.circle_vis = True
        self.score = 0
        self.score_text = arcade.Text(f"Score: {self.score}", 10, 570, color=arcade.color.BLACK_LEATHER_JACKET)
        
        def on_draw(self):
            self.clear()
            if self.circle_vis:
                arcade.draw_circle_filled(self.x, self.y, self.circle_radius, arcade.color.MAHOGANY)
        
        def on_mouse_press(self, x, y, button, modifiers):
            dx = x - self.x
            dy = y - self.y
            if dx * dx + dy * dy <= self.circle_radius **2:
                self.circle_vis = False
                self.score += 1

        def on_update(self, delta_time):
            self.score_text.text = f"Score: {self.score}"

def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()