import turtle as t
import random

raphael = t.Turtle()
raphael.shape("turtle")
raphael.color("red")
t.colormode(255)


def draw_square():
    for _ in range(4):
        raphael.forward(100)
        raphael.right(90)


def draw_dashed_line():
    for _ in range(50):
        raphael.forward(10)
        raphael.penup()
        raphael.forward(10)
        raphael.pendown()


sides = [3, 4, 5, 6, 7, 8, 9, 10]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def draw_shapes():
    for side in sides:
        counter = 0
        raphael.pencolor(random_color())
        while counter < side:
            side_angle = 360 / side
            raphael.right(side_angle)
            raphael.forward(100)
            counter += 1


distance = 50
direction = [0, 90, 180, 270]


def random_walk():
    for _ in range(250):
        raphael.speed("fastest")
        raphael.pensize(10)
        raphael.pencolor(random_color())
        raphael.forward(distance)
        raphael.setheading(random.choice(direction))


def draw_spirograph(size):
    for _ in range(int(360 / size)):
        raphael.pensize(3)
        raphael.speed("fastest")
        raphael.color(random_color())
        raphael.circle(100)
        raphael.setheading((raphael.heading() + size))


# draw_spirograph(10)
# random_walk()
# draw_shapes()
# draw_square()
# draw_dashed_line()


screen = t.Screen()
screen.exitonclick()
