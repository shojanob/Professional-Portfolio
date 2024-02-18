import random
import colorgram
from turtle import *
import turtle as t


tim = Turtle()
rgb_colors = []
colors = colorgram.extract('image.jpg', 12)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

color_list = [(137, 18, 201), (233, 253, 242), (251, 236, 247), (234, 240, 252), (40, 3, 179), (85, 251, 187), (224, 151, 108), (158, 3, 80), (5, 211, 91), (4, 139, 66), (240, 43, 125), (112, 103, 240)]
t.speed("fastest")
t.penup()
t.hideturtle()
t.colormode(255)
t.setheading(225)
t.forward(300)
t.setheading(0)
t.pendown()
number_of_dots = 100

for dot in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.penup()
    t.forward(50)
    t.pendown()

    if dot % 10 == 0:
        t.penup()
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)




screen = Screen()
screen.exitonclick()