import random
from turtle import Turtle

COLOR = ["red", "blue", "yellow", "purple", "orange", "cyan", "pink", "white"]


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.fillcolor("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        self.fillcolor(random.choice(COLOR))
        self.goto(random.randint(-270, 270), random.randint(-270, 270))
