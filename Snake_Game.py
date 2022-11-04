from  turtle import Screen
from Snake_Class import Snake
from Snake_Food import Food
from Snake_Scoreboard import ScoreBoard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title("Classic Snake Game")
screen.tracer(0)#turns off the screen

snake=Snake()
snake.create_snake()

food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect Collision with Food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.score_update()

    #Detect Collision with Wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on=False
        score.reset()
        snake.reset()
    #Detect collision with tail:
    #If the snake head collides with any part of the snake tail,then
    #it must trigger game over.
    for part in snake.snake_parts:
        if part==snake.head:
            pass
        elif snake.head.distance(part)<10:
            # game_is_on=False
            score.reset()
            snake.reset()

screen.exitonclick()
