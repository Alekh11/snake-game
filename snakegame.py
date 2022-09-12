from turtle import Turtle, Screen
from snake_sub import Snake
from food import Food 
from scoreboard import Scoreboard 
import time 


screen = Screen() 
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")



# segment1 = Turtle("square")
# segment1.color("white")
# segment2 = Turtle("square")
# segment2.color("white")
# segment2.goto(-20,0)
# segment3 = Turtle("square")
# segment3.color("white")
# segment3.goto(-40,0)
# The same thing can be done using for loop



game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    #screen's going to refresh every 0.2 seconds
    
    snake.move()
    
    #To delect collision w food we gotta check distance bw food and snake
    if snake.head.distance(food)<15:
       food.refresh() 
       scoreboard.increase_score()
       snake.extend()
       
    #On collision with wall:
    
    if snake.head.xcor()>290 or snake.head.xcor()<-300 or snake.head.ycor()>290 or snake.head.ycor()<-280:
        game_on = False
        scoreboard.gameover()

    #On collision with itself:
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_on = False
            scoreboard.gameover()


screen.exitonclick() 