from turtle import Screen
import time
from car_manager import CarManager
from scoreboard import Scoreboard
from player import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move()

    # Detect level up
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.level_up()
        car_manager.level_up()

    for car in car_manager.cars:
        if player.distance(car) < 20 and player.ycor() < FINISH_LINE_Y:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()