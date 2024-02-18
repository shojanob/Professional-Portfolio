import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            car_manager.car_collision()

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.next_level()
        car_manager.increase_level()

screen.exitonclick()