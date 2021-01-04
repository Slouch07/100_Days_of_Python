from turtle import Turtle, Screen
import random

# Create a screen object and set it size.
screen = Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput(title="Pick Your Winner!", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -75

race_turtles = []

# Turtle objects created and given a colour and starting point.
for colour in colours:
    turtle = Turtle(shape="turtle")
    turtle.color(colour)
    turtle.penup()
    turtle.goto(x=-240, y=y)
    y += 35
    race_turtles.append(turtle)

if user_choice:
    is_race_on = True

# Logic for when a turtle has crossed the finish line. 
is_race_on = False
while is_race_on:
    for turtle in race_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
