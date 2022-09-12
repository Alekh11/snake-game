from turtle import Turtle 
import random

foodcolor = ("red2", "maroon1", "goldenrod1", "red")
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 , stretch_wid=0.5)
        #reduced the len and width of circle from 20x20 to 10x10
        self.color(random.choice(foodcolor))
        self.speed("fastest")
        spawn_x = random.randint(-260,260)
        spawn_y = random.randint(-260,260)
        self.goto(spawn_x,spawn_y)
        
    def refresh(self):
        spawn_x = random.randint(-260,260)
        spawn_y = random.randint(-260,260)
        self.goto(spawn_x,spawn_y)
        