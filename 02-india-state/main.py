from turtle import Turtle, Screen
import pandas as pd

t = Turtle()
s = Screen()

IMG = "india_map.gif"

s.title("STATE GUESSING -- INDIA")
s.setup(width=655, height=750)
s.screensize(canvwidth=600, canvheight=700)
s.addshape(IMG)
t.shape(IMG)

data = pd.read_csv("india_state.csv")
all_states = data.state.to_list()
# print(all_states)


guessed_states = []
while len(guessed_states) < 29:
    answer_state = s.textinput(title=f"{len(guessed_states)}/{len(all_states)} States", prompt="Another state").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim = Turtle()
        tim.hideturtle()
        tim.pu()

        state_data = data[data.state == answer_state]
        # print(int(state_data.x.iloc[0]))

        tim.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        tim.write(answer_state)
    
    elif answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("learn_states.csv")
        break
