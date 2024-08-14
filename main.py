from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard


turtle = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)




r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  ball.move(l_paddle, r_paddle)
  if r_paddle.xcor() - 20 < ball.xcor() < r_paddle.xcor() + 20 and r_paddle.ycor() - 50 < ball.ycor() < r_paddle.ycor() + 50:
    scoreboard.r_point()
  if l_paddle.xcor() - 20 < ball.xcor() < l_paddle.xcor() + 20 and l_paddle.ycor() - 50 < ball.ycor() < l_paddle.ycor() + 50:
    scoreboard.l_point()
  if ball.xcor() > 350 or ball.xcor() < -350:
    scoreboard.end_game()




  

  


print(score)




screen.exitonclick()
