import time
from random import choice
from turtle import Screen
from player import Player
from obstacle_manager import ObstacleManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
obs = []
for i in range(0, 10):
    obs.append(ObstacleManager())
    
p = Player()
s = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    choice(obs).move()
    if p.distance(choice(obs)) < 50:
        screen.clear()
        s.game_over()
        game_is_on = False            
    if choice(obs).xcor() < -290:
        choice(obs).left_border()
        
    screen.onkeypress(p.move_forward, 'Up')
    screen.onkeypress(p.move_left, 'Left')
    screen.onkeypress(p.move_right, 'Right')
    screen.onkeypress(p.move_backward, 'Down')
    screen.listen()
    
    if p.xcor() < -100:
        p.left_border()
    if p.xcor() > 100:
        p.right_border()
    if p.ycor() == 280:
        p.hideturtle()
        p.goto(0, 280)
        p.check_position()
        p.showturtle()
        s.update_score()
    if p.ycor() < -280:
        p.bottom_border()
        
screen.exitonclick()