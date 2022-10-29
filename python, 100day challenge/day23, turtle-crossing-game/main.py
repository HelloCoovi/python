import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
cars = []


screen.onkey(player.go_up, "Up")

car_point = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.next_stage()


screen.exitonclick()

# 플레이어
#   게임 시작시 시작 포인트에서 시작하고
#   방향키 "Up"으로만 움직임
#   클리어시 원점으로
# 차량

# 게임 동작

