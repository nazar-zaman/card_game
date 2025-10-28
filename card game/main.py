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
        self.card_list_glcard_list_gl = []
        base_path = Path(__file__).parent
        for suit in ["clubs","hearts","spades","diamonds"]:
            for card_n in ["a",2,3,4,5,6,7,8,9,10,11,13,13]:
                filepath = f"{base_path}/images/{suit}/{str(card_n)}{suit[0]}.png"
                card_sprite = arcade.Sprite(filepath, scale=2.0)
                card_sprite.card_name = f"{str(card_n)}{suit[0]}"
                self.card_list.append(card_sprite)
                self.card_list_gl.append(f"{str(card_n)}{suit[0]}")
    
    def on_draw(self):
        self.clear()
        self.card_list.draw()

def main():
    game = CardGame()
    arcade.run()

if __name__ == "__main__":
    main()