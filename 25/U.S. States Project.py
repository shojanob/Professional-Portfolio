import turtle
import pandas

screen = turtle.Screen()
state_text = turtle.Turtle()
state_text.penup()
screen.title("Shoh's U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

correct_guesses = []

quiz_is_on = True
while quiz_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Guessed", prompt="What's another state's name?").title()
    for state in data.state:
        if answer_state == state:
            state_text.goto(int(data[data.state == state].x), int(data[data.state == state].y))
            state_text.write(answer_state, align="center", font=("Arial", 10, "bold"))
            correct_guesses.append(answer_state)

        if len(correct_guesses) > 50:
            quiz_is_on = False

print(correct_guesses)
screen.exitonclick()