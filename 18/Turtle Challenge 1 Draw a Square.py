from turtle import Turtle, Screen

tim = Turtle()
tim.shape("triangle")
tim.color("DarkGreen")

def draw_a_square():
    for _ in range (4):
        tim.forward(100)
        tim.right(90)



draw_a_square()




screen = Screen()
screen.exitonclick()