import turtle
from mimetypes import guess_type
from turtle import Turtle,Screen
import pandas

# Initialize the screen and turtle
screen = Screen()
tim = Turtle()

# Add background image of the US map
image = "blank_states_img.gif"
screen.addshape(image)
tim.shape(image)

writer = turtle.Turtle()

score = 0


# Load the dataset of states

df = pandas.read_csv("50_states.csv")
states_name = df.state.tolist()

writer.penup()
writer.hideturtle()

is_continue = 0
guessed_states = []

while len(guessed_states) < 50:
    """
      Main game loop:
      - Prompt the user to guess a US state.
      - If the guess is correct, display it on the map at the correct coordinates.
      - Keep track of score and guessed states.
      - Exit if the user types "Exit".
      """
    answer_text = screen.textinput(title=f"Us state Game {score}/50", prompt="Guess the state").title()

    if answer_text == "Exit":
        break
    if answer_text in states_name:
            guessed_states.append(answer_text)
            # Access the complete row for the guessed state
            state_row = df[df.state == answer_text]

            #fetch x and y axis
            x_axis = int(state_row.x.values[0])
            y_axis = int(state_row.y.values[0])

            # Move to position and write the state name
            writer.goto(x_axis,y_axis)
            writer.write(answer_text)

            #update score
            score += 1


# Generate a list of missing states (not guessed by the player)
missing_states = [state for state in states_name if state not in guessed_states]


# Save the missing states into a CSV file
"""
missing_states.csv will contain the names of states the player did not guess.
This can be used for learning or review later.
"""
missing_states_dict = {"names":missing_states}
dataframe = pandas.DataFrame(missing_states_dict)
dataframe.to_csv("missing_states.csv")