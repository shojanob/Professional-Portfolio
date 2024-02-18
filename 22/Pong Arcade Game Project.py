from scoreboard import Scoreboard
from turtle import *
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.title("Welcome to Shoh's Pong Arcade Game")
screen.bgcolor("black")
screen.tracer(0)


l_paddle = Paddle((-730, 0))
r_paddle = Paddle((730, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#   Detect collision with wall and bounce
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

#   Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 360 or
            ball.distance(l_paddle) < 50 and ball.xcor() < -360):
        ball.bounce_x()

#   Detect when ball goes past paddle
    if ball.xcor() > 750:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -750:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()