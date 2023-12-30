from turtle import Turtle
from random import choice, randint
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5


class ObstacleManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1.5, 3)
        self.color(choice(COLORS))
        self.setheading(180)
        self.goto(randint(-70,270),randint(-250, 250))
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
    
    def left_border(self):
            self.hideturtle()
            self.goto(x=randint(0, 280), y=randint(-250, 250))
            self.showturtle()