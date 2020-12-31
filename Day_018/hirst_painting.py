# A Python program that creates a painting of dots with random colours for each dot.

import turtle as t
import random

colour_list = [(229, 225, 221), (232, 206, 82), (225, 150, 88), (220, 228, 222), (228, 221, 224), (120, 167, 186),
               (158, 14, 20), (214, 223, 228), (33, 110, 158), (232, 83, 46), (123, 175, 144), (171, 20, 15),
               (7, 98, 37), (200, 63, 28), (185, 186, 27), (30, 129, 47), (12, 41, 75), (14, 64, 40), (243, 201, 5),
               (137, 81, 95), (84, 15, 22), (48, 167, 75), (44, 25, 21), (5, 65, 137), (171, 134, 149), (48, 150, 195),
               (232, 170, 161), (213, 65, 70), (74, 135, 186), (168, 207, 172), (165, 201, 211), (223, 172, 175),
               (176, 191, 212), (43, 72, 80), (249, 13, 8), (247, 13, 18), (64, 68, 53)]

leo = t.Turtle()
t.colormode(255)
leo.color("black")
leo.speed("fastest")
leo.hideturtle()

row = 0
y = -200
x = -200

while row < 10:
    leo.penup()
    leo.goto(x, y)
    for _ in range(10):
        leo.dot(20, random.choice(colour_list))
        leo.penup()
        leo.forward(50)
    row += 1
    y += 50


screen = t.Screen()
screen.exitonclick()
