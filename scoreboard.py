from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write(f"{self.l_score}      :      {self.r_score}", False, "center", ('Arial', 50, 'normal'))

    def reset_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}      :      {self.r_score}", False, "center", ('Arial', 50, 'normal'))