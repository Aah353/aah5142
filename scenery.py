from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

screen.setup(width=400, height=400)
screen.bgcolor('light green')

# Function to draw a leg of a table
def table_leg(color, short):
    """
    Draws a leg of the table.

    Parameters:
    color (str): The color of the leg.
    short (int): A shortening factor to make the rear legs appear behind the table.
    """
    t.pendown()
    t.color(color, color)
    t.begin_fill()
    t.right(90)
    t.forward(20 - short)
    t.right(90)
    t.forward(2)
    t.right(90)
    t.forward(20 - short)
    t.right(90)
    t.forward(2)
    t.end_fill()
    t.penup()

# Function to draw the table
def table(size, color):
    """
    Draws a table.

    Parameters:
    size (int): The length of the table.
    color (str): The color of the table.
    """
    t.penup()
    t.goto(-(size / 2), 0)
    t.pendown()

    t.color(color, color)
    t.begin_fill()

    # Draw table surface
    t.forward(size)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(10)
    t.right(90)

    t.end_fill()

    # Draw the four legs of the table
    t.penup()
    t.goto(-(size / 2) + 2, -10)
    table_leg(color, 0)
    t.goto(-(size / 2) + 7, -10)
    table_leg(color, 5)
    t.goto((size / 2), -10)
    table_leg(color, 0)
    t.goto((size / 2) - 5, -10)
    table_leg(color, 5)

    t.goto(0, 0)

# Function to draw one layer of the cake
def cake_layer(size, color, height):
    """
    Draws a single layer of the cake.

    Parameters:
    size (int): The width of the cake layer.
    color (str): The color of the cake layer.
    height (int): The height factor (used to reduce the height of each layer).
    """
    t.pendown()

    t.color(color, color)
    t.begin_fill()

    # Draw the cake layer
    t.forward(size)
    t.left(90)
    t.forward(size / height)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size / height)
    t.left(90)

    t.end_fill()

    t.left(90)
    t.forward(size / height)
    t.right(90)

    t.penup()

# Function to draw the cake
def cake(size):
    """
    Draws a multi-layered cake.

    Parameters:
    size (int): The width of the cake.
    """
    t.goto(-(size / 2), 0)

    # Prompt user for the color of each layer
    color1 = input("Enter the color for the first layer of the cake: ")
    color2 = input("Enter the color for the second layer of the cake: ")
    color3 = input("Enter the color for the third layer of the cake: ")
    color4 = input("Enter the color for the fourth layer of the cake: ")

    # Draw each layer of the cake with user-defined colors and heights
    cake_layer(size, color1, 8)
    cake_layer(size, color2, 10)
    cake_layer(size, color3, 5)
    cake_layer(size, color4, 4)

    t.color("white")
    t.goto(0, 0)

# Function to draw decorations on the cake
def decor(cake_size):
    """
    Draws decorations (cream and cherry) on the cake.

    Parameters:
    cake_size (int): The size of the cake for placing decorations.
    """
    # Position turtle for drawing decorations
    t.left(180)
    t.forward((cake_size / 2))
    t.right(90)
    t.forward(cake_size * (27 / 40))
    t.right(90)

    t.pendown()

    # Draw the cream decoration
    t.color("pink", "pink")
    t.begin_fill()
    radius = cake_size / 10
    t.right(90)
    t.forward(radius / 2)

    # Draw each cream curve without loops
    t.circle(radius, 180)
    t.left(180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(radius, 180)

    t.forward(radius / 2)
    t.left(90)
    t.forward(cake_size)
    t.end_fill()

    # Print message before drawing the cherry
    print("Let's not forget the cherry on top!")

    
    # Draw a cherry on top
    t.penup()
    t.left(180)
    t.forward(cake_size / 2)
    t.pendown()

    t.color("red", "red")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Draw candles
    # First candle
    t.penup()
    t.forward((cake_size / 4) + 2)
    t.pendown()

    t.color("yellow", "yellow")
    t.begin_fill()
    t.left(90)
    t.forward(cake_size / 3)
    t.left(90)
    t.forward(2)
    t.left(90)
    t.forward(cake_size / 3)
    t.left(90)
    t.forward(2)
    t.end_fill()

    # Draw the flame
    t.penup()
    t.forward(-1)
    t.left(90)
    t.forward(cake_size / 3)
    t.right(90)
    t.pendown()

    t.color("red", "red")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

    # Position for the second candle
    t.penup()
    t.right(90)
    t.forward(cake_size / 3)
    t.left(90)
    t.forward(1)

    # Second candle
    t.forward(-(cake_size / 2 + 2))
    t.pendown()

    t.color("yellow", "yellow")
    t.begin_fill()
    t.left(90)
    t.forward(cake_size / 3)
    t.left(90)
    t.forward(2)
    t.left(90)
    t.forward(cake_size / 3)
    t.left(90)
    t.forward(2)
    t.end_fill()

    # Draw the flame
    t.penup()
    t.forward(-1)
    t.left(90)
    t.forward(cake_size / 3)
    t.right(90)
    t.pendown()

    t.color("red", "red")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

    # Return to original position
    t.penup()
    t.right(90)
    t.forward(cake_size / 3)
    t.left(90)
    t.forward(1)

    t.right(90)
    t.forward(cake_size * (27 / 40))
    t.left(90)
    t.forward(cake_size / 2)

    


# Main function to draw the entire scene
def main(table_size, table_color, cake_size):
    """
    Main function to draw the scene: table, cake, and decorations.

    Parameters:
    table_size (int): The size of the table.
    table_color (str): The color of the table.
    cake_size (int): The size of the cake.
    """
    t.speed(10)

    # Draw table, cake, and decorations
    table(table_size, table_color)
    cake(cake_size)
    decor(cake_size)
    print("And Enjoy your cake!")
    screen.exitonclick()

# Prompt user for inputs through the terminal
table_size = int(input('Enter the size of a table (between 10-100): '))
table_color = input('Enter the color of the table: ')
cake_size = int(input('Enter the size of the cake (should be <= table size): '))
print("hold on a moment..")

# Run the main function
main(table_size, table_color, cake_size)

