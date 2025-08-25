import turtle
from mimetypes import guess_type
from turtle import Turtle,Screen
import pandas
screen = Screen()
tim = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
tim.shape(image)
writer = turtle.Turtle()

score = 0


df = pandas.read_csv("50_states.csv")
states_name = df.state.tolist()

writer.penup()
writer.hideturtle()
is_continue = 0
guessed_states = []
while len(guessed_states) < 50:
    answer_text = screen.textinput(title=f"Us state Game {score}/50", prompt="Guess the state").title()

    if answer_text == "Exit":
        break
    if answer_text in states_name:
            guessed_states.append(answer_text)
            #access the complete row
            state_row = df[df.state == answer_text]
            #fetch x and y axis
            x_axis = int(state_row.x.values[0])
            y_axis = int(state_row.y.values[0])
            writer.goto(x_axis,y_axis)
            writer.write(answer_text)
            score += 1



missing_states = [state for state in states_name if state not in guessed_states]

missing_states_dict = {"names":missing_states}
dataframe = pandas.DataFrame(missing_states_dict)
dataframe.to_csv("missing_states.csv")