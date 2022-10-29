from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

y_position = -120

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    new_turtle.color(color[i])
    y_position += 40
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! {winning_color} turtle is Winner!")
            else:
                print(f"You Lose! {winning_color} turtle is Winner!")

        rand_distnace = random.randint(0, 10)
        turtle.forward(rand_distnace)


screen.exitonclick()
