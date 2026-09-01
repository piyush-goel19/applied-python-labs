from turtle import Screen
import time
from Ball import Ball
from Scoreboard import Scoreboard
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

r_paddle = Paddle(360, 0)
l_paddle = Paddle(-370, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision of ball with upper walls and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision of ball with right paddle
    if (ball.xcor() > 340 and ball.distance(r_paddle) < 50) or (ball.xcor() < -350 and ball.distance(l_paddle) < 50):
        ball.reverse()

    if ball.xcor() > 370:
        ball.reset_ball()
        score.increase_lscore()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.increase_rscore()

screen.exitonclick()