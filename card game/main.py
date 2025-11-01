import arcade
from pathlib import Path
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Card Game"

class CardGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.LINCOLN_GREEN)
        self.card_list = arcade.SpriteList()
        self.back_list = arcade.SpriteList()
        self.card_list_gl = []
        self.player_cards = []
        self.computer_cards = []
        #filling up card list w/ sprites
        base_path = Path(__file__).parent
        for suit in ["clubs","hearts","spades","diamonds"]:
            for card_n in ["a",2,3,4,5,6,7,8,9,"t","j","q","k"]:
                filepath = f"{base_path}/images/{suit}/{str(card_n)}{suit[0]}.png"
                card_sprite = arcade.Sprite(filepath, scale=2.0)
                card_sprite.card_name = f"{str(card_n)}{suit[0]}"
                self.card_list.append(card_sprite)
                self.card_list_gl.append(f"{str(card_n)}{suit[0]}")
        #making seperate back sprite list for back cards for ease of animations
        #functional back card
        self.back1 = arcade.Sprite(f"{base_path}/images/back/back.png", scale = 2.0)
        self.back1.center_x = SCREEN_WIDTH/2
        self.back1.center_y = SCREEN_HEIGHT/2
        #unfunctional back card
        self.back2 = arcade.Sprite(f"{base_path}/images/back/back2.png", scale = 2.0)
        self.back2.center_x = SCREEN_WIDTH/2
        self.back2.center_y = SCREEN_HEIGHT/2
        #appending back sprites
        self.back_list.append(self.back2)
        self.back_list.append(self.back1)
        #making an all cards list for later
        self.all_cards = arcade.SpriteList()
        self.all_cards.extend(self.card_list)
        self.all_cards.extend(self.back_list)
        self.held_card = None
        
    def searchDeck(self, card, card_list):
        for sprite in card_list:
            if sprite.card_name == card:
                break
        return sprite
    
    def 
    
    def on_draw(self):
        self.clear()
        arcade.draw_line(0,200,1000,200,arcade.color.PAKISTAN_GREEN,5)
        self.back_list.draw()
        self.card_list.draw()
    
    def on_mouse_press(self, x, y, button, modifiers):
        self.held_card = arcade.get_sprites_at_point((x,y), )

            
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self

    def on_mouse_release(self, x, y, buttons, modifiers):
        self.held_card = None

    def on_update(self, delta):
        for card in self.card_list:
            if card.left < 0:
                card.left = 0
            if card.right > SCREEN_WIDTH:
                card.right = SCREEN_WIDTH
            if card.bottom < 0:
                card.bottom = 0
            if card.top > SCREEN_HEIGHT:
                card.bottom = SCREEN_HEIGHT



def main():
    game = CardGame()
    arcade.run()

if __name__ == "__main__":
    main()