from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Sneaky Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)
screen.onkeypress(key="Down", fun=snake.down)

game_is_on = True

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.06)
    snake.detect_food(food, scoreboard)
    if snake.detect_wall():
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
