from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Pick Your Winner!", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -75

for colour in colours:
    turtle = Turtle(shape="turtle")
    turtle.color(colour)
    turtle.penup()
    turtle.goto(x=-240, y=y)
    y += 35

screen.exitonclick()
