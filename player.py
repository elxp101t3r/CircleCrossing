from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape('circle')
        self.speed(8)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        
    def move_forward(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)
    
    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
            
    
    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
    
    def move_backward(self):
        self.setheading(90)
        self.backward(MOVE_DISTANCE)
    
    def left_border(self):
        self.move_right()
    
    def right_border(self):
        self.move_left()
        
    def bottom_border(self):
        self.move_forward()
        
    def check_position(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)