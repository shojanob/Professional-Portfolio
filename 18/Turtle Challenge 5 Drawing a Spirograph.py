import random
import turtle as t
from turtle import Screen
tim = t.Turtle()
tim.shape("triangle")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors

directions_b = [0, 90, 180, 270]
tim.speed("fastest")


for _ in range (45):
    tim.color(random_color())
    tim.circle(100)
    tim.left(10)



screen = Screen()
screen.exitonclick()
