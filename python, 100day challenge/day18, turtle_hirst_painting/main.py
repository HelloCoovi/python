# # TODO : 🎯Goal,
# 가로세로 10 합 100개의 점을 찍는다.
# 점의 크기: 20, 점 간 거리: 50

# 색상 추출을 위해 사용했던 코드이며 코드를 리스트화했으므로 필요없다.
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = r, g, b
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed(0)
screen = Screen()
turtle.colormode(255)

rgb_colors = [(244, 244, 243), (241, 244, 249), (248, 241, 245), (240, 247, 244), (246, 157, 50), (51, 79, 168), (235, 62, 109), (169, 186, 2), (174, 21, 65), (63, 40, 56), (252, 211, 12), (251, 86, 41), (240, 125, 168), (82, 168, 213), (2, 97, 81), (3, 168, 203), (34, 60, 136), (252, 210, 0), (193, 35, 54), (65, 41, 39), (236, 162, 186), (9, 71, 60), (161, 73, 53), (58, 112, 104), (137, 178, 155), (110, 119, 166), (241, 165, 155), (182, 181, 218), (29, 43, 82), (145, 210, 226)]

def pick_color():
    return random.choice(rgb_colors)

timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, pick_color())
        timmy.forward(50)

    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


# timmy.home()


screen.exitonclick()