import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Card Game"

sprite_list = arcade.SpriteList()
for suit in ["clubs","hearts","spades","diamonds"]:
    for card_n in ["a",2,3,4,5,6,7,8,9,10,11,13,13]:
        filepath = f"/home/italyisashaitaly/vs code/card game/images/{suit}/{str(card_n)}{suit[0]}.png"
        sprite = arcade.Sprite(filepath, scale=1.0)
        sprite_list.append(sprite)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

        # Circle state
        self.circle_x = 400
        self.circle_y = 300
        self.circle_radius = 40
        self.circle_visible = True

        # Score
        self.score = 0

    def on_draw(self):
        self.clear()
        if self.circle_visible:
            arcade.draw_circle_filled(self.circle_x, self.circle_y,self.circle_radius, arcade.color.RED)
        arcade.draw_text(f"Score: {self.score}", 10, 570,arcade.color.WHITE, 20)

    def on_mouse_press(self, x, y, button, modifiers):
        # Check if click is inside the circle
        dx = x - self.circle_x
        dy = y - self.circle_y
        if dx * dx + dy * dy <= self.circle_radius ** 2:
            self.circle_visible = False
            self.score += 1

def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()