import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Put in your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [100, 70, 40, 10, -20, -50]
all_turtles = []




for t_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinates[t_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won your bet! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost your bet. The {winning_color} turtle is the winner.")
        random_dist = random.randint(0,10)
        turtle.forward(random_dist)



screen.exitonclick()