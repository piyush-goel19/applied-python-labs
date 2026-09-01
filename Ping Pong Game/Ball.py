from turtle import Turtle

START_POS = (0,0)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce(self):
        self.y_move *= -1

    def reverse(self):
        self.x_move *= -1
        self.move_speed -= 0.1 * self.move_speed

    def reset_ball(self):
        self.goto(START_POS)
        self.move_speed = 0.1
        self.reverse()
