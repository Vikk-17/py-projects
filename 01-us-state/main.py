from turtle import Turtle, Screen
import pandas as pd

FONT = 'monaco', 10, "bold"
IMG = "blank_states_img.gif"

# Screen Setup

t = Turtle()
screen = Screen()
screen.title("US STATE GAME")
screen.addshape(IMG)
t.shape(IMG)

# -->

# Read Data from csv with corresponding user input

data = pd.read_csv("50_states.csv")

# -->

# make a list of all the states
all_states = data.state.to_list()

# -->

# list that you have guessed
guessed_list = []

while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 states", 
                                prompt="Another state").title()
    
    # match the user input if it is in states list
    if answer_state in all_states:
        guessed_list.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state, font=FONT)
    
    # exit the game and make list of missed states
    elif answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_list:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("learn_states.csv")
        break

