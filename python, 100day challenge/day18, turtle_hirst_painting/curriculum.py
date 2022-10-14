import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color("red")

# # TODO 1, 정사각형 그리기
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
#
# # TODO 2, 점선 그리기
# for _ in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# # TODO 3, 다양한 도형 그리기(3,4,5,6,7,8,9,10각형까지)
# 각 변의 길이는 100
# 각 도형의 총 내각 크기는 삼각형은 180 사각형은 360으로 180씩 증가한다.
# challenge🦾: 도형이 그려질때마다 선의 색을 바꿔보세요
# import random
#
# screen.colormode(255)
#
# def random_color():
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     return r, g, b
#
# # 내각이 아니라 외각의 크기가 언제나 360이라는 것을 알고 풀어보자
# # 기존 코드는 내각을 이용한 코드였기때문에
# # 회전각을 180 - (각 / 꼭지점) 과 같이 비효율적으로 구했음
# # 외각은 크기가 언제나 360이라는 점을 기억하자
# vertex = 3
#
# for i in range(8):
#     timmy.color(random_color())
#     for j in range(vertex):
#         timmy.forward(100)
#         timmy.right(360 / vertex)
#     vertex += 1

# # TODO 4, 무작위 방향(사방)으로 움직이는 터틀 만들기
# 선의 굵기는 굵게, 속도는 높이고, 방향을 전환할때마다 색이 변한다.
# import random
#
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     return (r, g, b)
#
# timmy.speed(10)
# timmy.pensize(10)
# direction = [0, 90, 180, 270]
#
# while True:
#     timmy.color(random_color())
#     timmy.right(random.choice(direction))
#     timmy.forward(30)

# # TODO 5, 원 100개를 그리는 터틀 구현
# 그릴때마다 선색이 변하고 각도를 조금씩 조정해서 100개의 원을 그린다.
import random

turtle.colormode(255)
timmy.speed(0)

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b

for _ in range(100):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(360/100)

# 터틀 창이 꺼지지않게 하기위한 함수 모든 과제에 공통 적용이므로 그냥 두자
screen.exitonclick()