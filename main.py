from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ultimate Pong")
screen.bgcolor("black")
screen.tracer(0)
delay = 0.1

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(l_paddle.move_paddle_up, "w")
screen.onkey(l_paddle.move_paddle_down, "s")
screen.onkey(r_paddle.move_paddle_up, "Up")
screen.onkey(r_paddle.move_paddle_down, "Down")

while game_is_on:
    screen.update()
    time.sleep(delay)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    if 325 <= ball.xcor() <= 330 or -330 <= ball.xcor() <= -325:
        if ball.distance(r_paddle) < 60:
            ball.bounce_x()
            delay *= 0.9
        elif ball.distance(l_paddle) < 60:
            ball.bounce_x()
            delay *= 0.9

    if ball.xcor() > 400:
        ball.ball_reset()
        scoreboard.l_score += 1
        scoreboard.reset_scoreboard()
        delay = 0.1

    if ball.xcor() < -400:
        ball.ball_reset()
        scoreboard.r_score += 1
        scoreboard.reset_scoreboard()
        delay = 0.1

screen.exitonclick()

