from turtle import Turtle
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()
    def update_level(self):
        self.clear()
        self.goto(-270, 240)
        self.write(f"Level: {self.level}", align="left", font=(FONT))

    def next_level(self):
        self.level += 1
        self.update_level()

