from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "blue", "green", "yellow", "orange", "purple"]

turtles = []

def create_turtle(color):
    t = Turtle("turtle")
    t.color(color)
    return t

for i in range(6):
    tl = create_turtle(colors[i])
    tl.up()
    tl.goto(-230,-100 + (i*40))
    turtles.append(tl)

user_bet = screen.textinput(title="Choose your bet", prompt="Which turtle will win the race? Enter color: ")
print(user_bet)

winner = ""

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_dist = random.randint(0,10)
        turtle.penup()
        turtle.forward(random_dist)
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            screen.clearscreen()

if winner == user_bet:
    print("You win!")
else:
    print(f"You lose! Winner is {winner} turtle")

screen.exitonclick()
