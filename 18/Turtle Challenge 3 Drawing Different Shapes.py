import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("triangle")
colors = ["Black", "Red", "Blue", "LightSeaGreen", "DarkSlateGray", "DarkOrange", "Cyan", "SaddleBrown"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side)


screen = Screen()
screen.exitonclick()