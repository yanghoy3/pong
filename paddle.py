from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcoor):
        super(Paddle, self).__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(xcoor, 0)

    def move_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto((self.xcor(), new_y))

    def move_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto((self.xcor(), new_y))
