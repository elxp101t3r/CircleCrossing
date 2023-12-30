from turtle import Turtle
from player import Player
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.score = 0
        self.write(f'Level:{self.score}', font=FONT, align='center')
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Level:{self.score}', font=FONT, align='center')
    
    def game_over(self):
        self.clear()
        self.goto(-90,0)
        self.write('Game Over!', font=FONT)
        