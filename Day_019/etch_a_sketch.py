from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    leo.forward(10)


def move_backwards():
    leo.backward(10)


def move_counter_clockwise():
    leo.left(5)


def move_clockwise():
    leo.right(5)


def clear_drawing():
    leo.clear()
    leo.penup()
    leo.home()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
