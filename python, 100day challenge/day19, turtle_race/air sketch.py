from turtle import Turtle, Screen

# 'w'를 누르면 앞으로
# 's'를 누르면 뒤로
# 'a'를 누르면 왼쪽으로 회전
# 'd'를 누르면 오른쪽으로 회정
# 'c'를 누르면 초기화

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.reset()

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()