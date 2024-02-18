import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
rand_y = random.randint(-260, 260)
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_prob = random.randint(1,6)
        if random_prob == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(320,random.randint(-260,260))
            self.cars.append(new_car)

    def increase_level(self):
        self.car_speed += MOVE_INCREMENT

    def move_car(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def car_collision(self):
        self.write("GAME OVER.", align="center", font=("Arial", 18, "bold"))

