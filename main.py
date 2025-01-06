from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("PONG GAME")
screen.setup(800, 600)
screen.tracer(0)


p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(p1.go_up, "Up")
screen.onkey(p1.go_down, "Down")
screen.onkey(p2.go_up, "w")
screen.onkey(p2.go_down, "s")




game_is_on  = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(p1) < 50 and ball.xcor() > 320) or (ball.distance(p2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        tim = Turtle()
        tim.color("white")
        tim.goto(-110, 0)
        if scoreboard.l_score == 5:
            tim.write(f"A has won!!", "center", font=("Courier", 30, "normal"))
            game_is_on = False
        elif scoreboard.r_score == 5:
            tim.write(f"B has won!!", "center", font=("Courier", 30, "normal"))
            game_is_on = False



screen.exitonclick()

