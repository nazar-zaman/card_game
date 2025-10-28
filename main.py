import arcade
print("Running new main.py")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "My first arcade window"

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.AMAZON)
    arcade.start_render()
    arcade.draw_circle_filled(100,100,20,arcade.color.RED)
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()