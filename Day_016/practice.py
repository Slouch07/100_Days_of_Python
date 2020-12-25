# from turtle import Turtle, Screen
#
# leonardo = Turtle()  # Creates new turtle object
# leonardo.shape("turtle")  # Create a 'turtle' icon on the canvas.
# leonardo.color("green4")  # Changes the turtles colour.
# leonardo.forward(100)  # Moves the turtle forward by 100.
#
# my_screen = Screen()  # Creates a new Screen object and places it in my_screen.
# print(my_screen.canvheight)  # Prints the screens current height.
# my_screen.exitonclick()  # The screen will only close when clicked within.

from prettytable import PrettyTable
table = PrettyTable()  # Create new PrettyTable object
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])  # Creates a new column heading with data.
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"  # Aligns the text to the left side of the column.
print(table)