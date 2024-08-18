from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
SWIDTH = 800
SHEIGHT = 600
BGCOLOR = "black"
STITLE = "pong"
# TODO 1: Create the screen
screen = Screen()
screen.setup(width=SWIDTH, height=SHEIGHT)
screen.bgcolor(BGCOLOR)
screen.title(STITLE)
screen.tracer(0)
# TODO 2: Create and move a paddle
# TODO 3: Create another paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# TODO 4: Create the ball and make it move
ball = Ball()
scoreboard = Scoreboard()


screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

screen.listen()
score = 0
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO 5: Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# TODO 6: Detect collision with paddle
    #Detect collision w/ right paddle and collision with left paddle
    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() > -320:
        ball.bounce_x()

# TODO 7: Detect when paddle misses
# TODO 8: Keep score
    # right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # #left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
