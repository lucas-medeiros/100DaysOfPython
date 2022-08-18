# @author   Lucas Cardoso de Medeiros
# @since    30/06/2022
# @version  1.0

# US States Game

import turtle
import pandas

IMAGE_PATH = "blank_states_img.gif"
DATA_PATH = "50_states.csv"
LEARN_STATES_PATH = "states_to_learn.csv"
ALIGN = "center"
FONT = ("Arial", "12", "normal")


def write_state(state, x, y):
    new_state = turtle.Turtle()
    new_state.hideturtle()
    new_state.penup()
    new_state.color("black")
    new_state.speed("fastest")
    new_state.goto(x, y)
    new_state.write(arg=f"{state}", move=False, align=ALIGN, font=FONT)


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)
correct = []
missing_states = {
    "States to learn": []
}

data = pandas.read_csv(DATA_PATH)
game_on = True

while len(correct) < 50:
    guess = screen.textinput(title=f"{len(correct)}/50 States Correct", prompt="What's another state's name?").title()
    if guess == "Exit":
        for row in data.state:
            if row not in correct:
                missing_states["States to learn"].append(row)
        df = pandas.DataFrame(missing_states)
        df.to_csv(LEARN_STATES_PATH)
        break
    state = data[data.state == guess]
    if state.empty:
        print("State doesn't exist!")
    else:
        if guess not in correct:
            write_state(state.state.item(), int(state.x), int(state.y))
            correct.append(state.state.values[0])
            print("Nice!")
        else:
            print("Already guessed this state")
print(f"Congratulations! You guessed {len(correct)}/50 states!")
