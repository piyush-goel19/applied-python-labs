import turtle

import colorgram
from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
turtle.colormode(255)
print(screen.canvheight, screen.canvwidth)
#t.teleport(-150, -150)

# colors = colorgram.extract("image.jpg", 30)
# # print(colors[0])
# # print(colors[0].rgb)
# # print(colors[0].hsl)
# # print(colors[0].proportion)
# color_tuple_lists = []
# for color in colors:
#     rgb = color.rgb
#     red, green, blue = rgb.r, rgb.g, rgb.b
#     color_tuple = (red, green, blue)
#     color_tuple_lists.append(color_tuple)
#
# print(color_tuple_lists)

colors_list = [(245, 243, 239), (247, 242, 244), (204, 164, 107), (239, 245, 241), (155, 73, 46), (235, 238, 244), (52, 92, 123), (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), (163, 142, 158), (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90), (144, 21, 24), (41, 62, 74), (82, 145, 128), (181, 87, 89), (41, 66, 90), (13, 71, 68), (213, 178, 183), (179, 191, 207)]

def hirst_dot_painting():
    t.speed("fastest")
    grid = [250, 250]
    for y in range(-250, grid[0], 50):
        for x in range(-250, grid[1], 50):
            random_color = random.choice(colors_list)
            t.up()
            t.goto(x, y)
            t.dot(20, random_color[0], random_color[1], random_color[2])
    t.hideturtle()

# t.setheading(225)
# t.fd(250)
# t.setheading(0)

hirst_dot_painting()
screen.exitonclick()