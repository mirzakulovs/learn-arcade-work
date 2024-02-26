import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.BLUEBERRY)


def draw_house():
    # Draw the house body
    arcade.draw_rectangle_filled(250, 200, 200, 100, arcade.color.COFFEE)

    # Draw the roof
    arcade.draw_triangle_filled(250, 400, 100, 250, 400, 250, arcade.color.COOL_GREY)

    # Draw the door
    arcade.draw_rectangle_filled(250, 190, 40, 80, arcade.color.AUBURN)

    # Draw the window
    arcade.draw_rectangle_filled(250, 300, 40, 40, arcade.color.DANDELION)


def draw_snow_person():
    # Draw snow person
    arcade.draw_circle_filled(600, 120, 70, arcade.color.WHITE)
    arcade.draw_circle_filled(600, 230, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(600, 310, 40, arcade.color.WHITE)
    arcade.draw_point(590, 320, arcade.color.BLACK, 10)
    arcade.draw_point(610, 320, arcade.color.BLACK, 10)
    arcade.draw_line(590, 300, 610, 300, arcade.color.ORANGE, 6)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
    arcade.start_render()

    draw_grass()
    draw_house()
    draw_snow_person()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
