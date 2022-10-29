from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-240, 255)
        self.write(f"LEVEL{self.level}", align="center", font=FONT)

    def next_stage(self):
        self.clear()
        self.level += 1
        self.write(f"LEVEL{self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
