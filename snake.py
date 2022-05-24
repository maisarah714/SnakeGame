from turtle import Turtle

SNAKE_INITIAL_LEN = 3
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in range(0, SNAKE_INITIAL_LEN):
            position = (i * -20, 0)
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle('square')
        new_snake.penup()
        new_snake.goto(position)
        new_snake.color('white')
        self.segment.append(new_snake)

    def reset(self):
        for seg in self.segment:
            seg.reset()
        self.__init__()


    def extends(self):
        self.add_segment(self.segment[-1].pos())

    def move(self):
        for index in range(len(self.segment) - 1, 0, -1):
            self.segment[index].goto(self.segment[index - 1].pos())

        self.head.forward(MOVE_DISTANCE)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
