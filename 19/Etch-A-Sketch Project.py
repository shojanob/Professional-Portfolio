from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)

def rotate_counter_clockwise():
    tim.left(10)
def rotate_clockwise():
    tim.right(10)

def clear_drawing():
    tim.clear()
def reset_sketch():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="v", fun=reset_sketch)


screen.exitonclick()