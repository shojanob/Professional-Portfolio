from turtle import *

tim = Turtle()
tim.shape("triangle")
tim.color("DarkGreen")
screen = Screen()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen.exitonclick()