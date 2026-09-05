from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

def create_turtle():
    t = Turtle()
    t.hideturtle()
    t.penup()
    return t
# def get_mouse_click_pos(x,y):
#    print(x,y)
#
# screen.onscreenclick(get_mouse_click_pos)
# screen.mainloop()
data = pd.read_csv("50_states.csv")
states_list = data["state"].to_list()
xcor_list = data["x"].to_list()
ycor_list = data["y"].to_list()

guessed_states = []

score = 0
while score < 50:
    if score == 0:
        user_guess = screen.textinput(title="Guess the state", prompt="Enter a state name?").title()
    else:
        user_guess = screen.textinput(title=f"{score}/50 States Correct", prompt="Enter a state name?").title()
    if user_guess == "Exit":
        break
    if user_guess in states_list:
        index = states_list.index(user_guess)
        pos = (xcor_list[index], ycor_list[index])
        new_turtle = create_turtle()
        new_turtle.goto(pos)
        new_turtle.write(user_guess, align="center", font=("Arial", 10, "normal"))
        score += 1
        guessed_states.append(user_guess)


#screen.exitonclick()

#save missing states to csv
print(guessed_states)
missing_states = []
for state in states_list:
    if state not in guessed_states:
        missing_states.append(state)

print(missing_states)
df = pd.DataFrame(missing_states)
df.to_csv("states_to_learn.csv")