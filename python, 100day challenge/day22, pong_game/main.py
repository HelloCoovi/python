import time
from turtle import Turtle
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # Detect collidion with r_paddel
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # Detect miss ball
    if ball.xcor() > 390:
        ball.home()
        ball.bounce_paddle()
        scoreboard.l_score += 1
        scoreboard.updata_scoreboard()
        ball.move_speed = 0.05

    if ball.xcor() < -390:
        ball.home()
        ball.bounce_paddle()
        scoreboard.r_score += 1
        scoreboard.updata_scoreboard()
        ball.move_speed = 0.05


screen.exitonclick()

# 화면 만들기
# 패들 움직이기
# 다른 패들 만들기
# 공 만들기, 공이 움직이기
# 공이 벽에 부딪히는거 감지, 튕김
# 공이 패들에 부딪히는지 감지, 튕김
# 패들이 공을 놓치는지 확인
# 점수 업데이트


