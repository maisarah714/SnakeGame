from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.display_scoreboard()

    def display_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.display_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
