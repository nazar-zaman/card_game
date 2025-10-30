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
        base_path = Path(__file__).parent
        for suit in ["clubs","hearts","spades","diamonds"]:
            for card_n in ["a",2,3,4,5,6,7,8,9,10,11,12,13]:
                filepath = f"{base_path}/images/{suit}/{str(card_n)}{suit[0]}.png"
                card_sprite = arcade.Sprite(filepath, scale=2.0)
                card_sprite.card_name = f"{str(card_n)}{suit[0]}"
                self.card_list.append(card_sprite)
                self.card_list_gl.append(f"{str(card_n)}{suit[0]}")
        self.back1 = arcade.Sprite(f"{base_path}/images/back/back.png", scale = 2.0)
        self.back1.center_x = SCREEN_WIDTH/2
        self.back1.center_y = SCREEN_HEIGHT/2
        self.back2 = arcade.Sprite(f"{base_path}/images/back/back2.png", scale = 2.0)
        self.back2.center_x = SCREEN_WIDTH/2
        self.back2.center_y = SCREEN_HEIGHT/2
        self.back_list.append(self.back2)
        self.back_list.append(self.back1)
        self.held_card = None
        
    def searchDeck(self, card, card_list):
        for sprite in card_list:
            if sprite.card_name == card:
                break
        return sprite
    
    def on_draw(self):
        self.clear()
        arcade.draw_line(0,200,1000,200,arcade.color.PAKISTAN_GREEN,5)
        self.card_list.draw()
        self.back_list.draw()
    
    def on_mouse_press(self, x, y, button, modifiers):
        self.cards_selected = arcade.get_sprites_at_point((x, y), self.card_list)
        if len(self.cards_selected) != 0:
            self.held_card = self.cards_selected[-1]
            self.card_list.remove(self.held_card)
            self.card_list.append(self.held_card)
        self.back_selected = arcade.get_sprites_at_point((x,y) , self.back_list)
        if len(self.back_selected) != 0:
            self.back1.visible = False
            random.shuffle(self.card_list_gl)
            self.top_card_gl = self.card_list_gl[-1]
            self.card_list_gl.remove(self.top_card_gl)
            self.player_cards.append(self.top_card_gl)
            top_card = self.searchDeck(self.top_card_gl, self.card_list)
            top_card.center_x = SCREEN_WIDTH/2
            top_card.center_y = SCREEN_HEIGHT/2

            
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