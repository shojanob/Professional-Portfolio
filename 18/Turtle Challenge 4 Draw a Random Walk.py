from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("triangle")

colors = ["Black", "Red", "Blue", "LightSeaGreen", "DarkSlateGray", "DarkOrange", "Cyan", "SaddleBrown"]
directions_a = ["forward", "backward", "right", "left"]
directions_b = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")

# One way to do it
for _ in range(200):
     tim.color(random.choice(colors))
     random_direction = random.choice(directions_a)
     if random_direction == "forward":
         tim.forward(25)
     elif random_direction == "backward":
         tim.backward(25)
     elif random_direction == "right":
         tim.right(25)
     else:
         tim.left(25)

# Another way to do it
for _ in range (200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions_b))


screen = Screen()
screen.exitonclick()