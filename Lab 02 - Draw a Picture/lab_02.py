"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(700, 700, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 799
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, arcade.color.DARK_PASTEL_GREEN)
# Draw a sun
arcade.draw_circle_filled(500, 550, 50, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# Draw the house body
arcade.draw_rectangle_filled(250, 200, 200, 100, arcade.color.ARSENIC)

# Draw the roof
arcade.draw_triangle_filled(250, 400, 100, 250, 400, 250, arcade.color.GRAY)

# Draw the door
arcade.draw_rectangle_filled(250, 190, 40, 80, arcade.color.AUBURN)

# Draw the window
arcade.draw_rectangle_filled(250, 300, 40, 40, arcade.color.CELADON_BLUE)

# Draw the cloud
arcade.draw_circle_filled(100, 600, 40, arcade.color.WHITE)
arcade.draw_circle_filled(140, 600, 50, arcade.color.WHITE)
arcade.draw_circle_filled(180, 600, 40, arcade.color.WHITE)
arcade.draw_circle_filled(120, 570, 40, arcade.color.WHITE)
arcade.draw_circle_filled(160, 570, 40, arcade.color.WHITE)

# Draw another cloud
arcade.draw_circle_filled(300, 500, 40, arcade.color.WHITE)
arcade.draw_circle_filled(340, 500, 50, arcade.color.WHITE)
arcade.draw_circle_filled(380, 500, 40, arcade.color.WHITE)
arcade.draw_circle_filled(320, 470, 40, arcade.color.WHITE)
arcade.draw_circle_filled(360, 470, 40, arcade.color.WHITE)

# Draw the tree trunk
arcade.draw_rectangle_filled(550, 160, 40, 100, arcade.color.DARK_BROWN)

# Draw the tree body
arcade.draw_triangle_filled(450, 150, 550, 300, 650, 150, arcade.color.DARK_GREEN)
arcade.draw_triangle_filled(460, 250, 550, 375, 640, 250, arcade.color.DARK_GREEN)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
