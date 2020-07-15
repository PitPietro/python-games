import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

"""
The Window class

Larger programs will typically derive from the Window class, or use decorators. This allows a programmer to write code to handle drawing, updating, and handling input from the user. A template for a starting a Window-based program is below.

The Window class has several methods that your programs can override to provide functionality to the program. Here are some of the most commonly used ones:

    on_draw: All the code to draw the screen goes here.
    update: All the code to move your items and perform game logic goes here. This is called about 60 times per second.
    on_key_press: Handle events when a key is pressed, such as giving a player a speed.
    on_key_release: Handle when a key is released, here you might stop a player from moving.
    on_mouse_motion: This is called every time the mouse moves.
    on_mouse_press: Called when a mouse button is pressed.
    set_viewport: This function is used in scrolling games, when you have a world much larger than what can be seen on one screen. Calling set_viewport allows a programmer to set what part of that world is currently visible.

"""
