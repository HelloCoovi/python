from turtle import Turtle, Screen

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=('Arial', 20, 'normal'))

    def eat_food(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))



