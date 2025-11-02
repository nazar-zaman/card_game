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
        self.card_list_gl= []
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
        #making seperate back sprite list for back cards for easy of animations
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
        self.update_key = "computer turn"

    def shuffle(self, sprite_list):
        card_list = list(sprite_list)
        random.shuffle(card_list)
        for sprite in card_list:
            sprite_list.append(sprite)

        
    def search_deck(self, card, card_list):
        for sprite in card_list:
            if sprite.card_name == card:
                break
        return sprite
    
    def generateCard(self):
        self.shuffle(self.card_list)
        generated_card = self.card_list[-1]
        self.card_list.remove(generated_card)
        self.player_cards.append(generated_card)
        sprite = self.search_deck(generated_card, self.card_list)
        sprite.center_x = SCREEN_WIDTH/2
        sprite.center_y = SCREEN_HEIGHT/2

    def player_pickup(self, x, y):
        self.held_cards = arcade.get_sprites_at_point((x,y), self.card_list)
        if len(self.held_cards) > 0:
            self.held_card = self.held_cards[-1]
            self.card_list.remove(self.held_card)
            self.card_list.append(self.held_card)
            return
        self.poss_held_backs = arcade.get_sprites_at_point((x,y), self.all_cards)
        if len(self.poss_held_backs) > 0:
                self.generateCard()

    def computer_pickup(self):
        self.shuffle(self.card_list)
        self.computer_cards.append(self.card_list[-1])
        self.update_key ="computer turn"

    
    def on_draw(self):
        self.clear()
        arcade.draw_line(0,200,1000,200,arcade.color.PAKISTAN_GREEN,5)
        self.back_list.draw()
        self.card_list.draw()
    
    def on_mouse_press(self, x, y, button, modifiers):
        self.held_cards = arcade.get_sprites_at_point((x,y), self.card_list)
        if len(self.held_cards) > 0:
            self.held_card = self.held_cards[-1]
            self.card_list.remove(self.held_card)
            self.card_list.append(self.held_card)
        

            
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.held_card != None:
            self.held_card.center_x += dx
            self.held_card.center_y += dy

    def on_mouse_release(self, x, y, buttons, modifiers):
        self.held_card = None
        self.top_card_back = None

    def on_update(self, delta):
        if self.update_key == "computer turn":
            self.back1.center_y += 5
            if self.back1.bottom == SCREEN_HEIGHT:
                self.update_key = None
                self.back1.center_x = SCREEN_WIDTH/2
                self.back1.center_y = SCREEN_HEIGHT/2

        for card in self.card_list_sp:
            if card.left < 0:
                card.left = 0
            if card.right > SCREEN_WIDTH:
                card.right = SCREEN_WIDTH
            if card.bottom < 0:
                card.bottom = 0
            if card.top > SCREEN_HEIGHT and card != self.back1:
                card.top = SCREEN_HEIGHT
        




def main():
    game = CardGame()
    arcade.run()

if __name__ == "__main__":
    main()