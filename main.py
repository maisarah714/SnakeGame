import time
from turtle import Turtle, Screen
from snake import Snake
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(key='Right', fun=snake.turn_right)
screen.onkey(key='Left', fun=snake.turn_left)
screen.onkey(key='Up', fun=snake.turn_up)
screen.onkey(key='Down', fun=snake.turn_down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
