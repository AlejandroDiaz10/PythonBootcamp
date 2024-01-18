import pandas
import turtle

us_data = pandas.read_csv("50_states.csv")
us_states = us_data.state.tolist()

my_screen = turtle.Screen()
my_screen.title("U.S. States Game")
my_image = "blank_states_img.gif"
my_screen.addshape(my_image)
turtle.shape(my_image)

# Function to get the coordenates of all the states
# def get_coordenates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_coordenates)
# turtle.mainloop()

answers_list = []

while len(answers_list) < 50:
    answer_state = my_screen.textinput(
        title=f"{len(answers_list)}/50 Guess the state",
        prompt="What's another state's name? or 'Exit'",
    ).title()

    if answer_state == "Exit":
        break

    if answer_state in us_states and answer_state not in answers_list:
        answers_list.append(answer_state)
        state = us_data[us_data.state == answer_state].iloc[0]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer_state)

        # Both options are valid: .values[0] or .item()
        # x_cor = int(us_data[us_data.state == answer_state].x.values[0])
        # y_cor = int(us_data[us_data.state == answer_state].y.item())
        # t.goto(x_cor, y_cor)

# states_missing_list = list(set(us_states) - set(answers_list)) # Option 1
states_missing_list = [state for state in us_states if state not in answers_list]
pandas.DataFrame(states_missing_list).to_csv("states_missing.csv")
