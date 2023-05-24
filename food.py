import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.generate_food()

    def generate_food(self):
        random_x = random.randint(-390, 390)
        random_y = random.randint(-390, 390)
        self.goto(random_x, random_y)