import arcade
from pathlib import Path
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Card Game"

class CardGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)
        
        self.card_list = arcade.SpriteList()
        self.card_list_gl = []
        base_path = Path(__file__).parent
        for suit in ["clubs","hearts","spades","diamonds"]:
            for card_n in ["a",2,3,4,5,6,7,8,9,10,11,13,13]:
                filepath = f"{base_path}/images/{suit}/{str(card_n)}{suit[0]}.png"
                card_sprite = arcade.Sprite(filepath, scale=2.0)
                card_sprite.card_name = f"{str(card_n)}{suit[0]}"
                self.card_list.append(card_sprite)
                self.card_list_gl.append(f"{str(card_n)}{suit[0]}")
        self.held_card = None
    
    def on_draw(self):
        self.clear()
        self.card_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        cards_selected = arcade.get_sprites_at_point((x, y), self.card_list)
        if len(cards_selected) != 0:
            self.held_card = cards_selected[-1]
            self.card_list.remove(self.held_card)
            self.card_list.append(self.held_card)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.held_card != None:
            if self.held_card.collides_with_point((x, y)):
                self.held_card.center_x += dx
                self.held_card.center_y += dy

    def on_mouse_release(self, x, y, buttons, modifiers):
        self.held_card = None



def main():
    game = CardGame()
    arcade.run()

if __name__ == "__main__":
    main()