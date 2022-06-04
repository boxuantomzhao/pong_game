from turtle import Turtle, Screen
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):

    def __init__(self,paddle_len,start_position,speed):
        super().__init__() # Inherent from turtle class
        self.start_position = start_position
        self.paddle_len = paddle_len
        self.speed = speed
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=self.paddle_len, stretch_len=1)
        self.penup()
        self.goto(self.start_position)

    def move_up(self):
        new_y = self.ycor() + self.speed
        self.setposition(x=self.start_position[0], y=new_y)

    def move_down(self):
        new_y = self.ycor() - self.speed
        self.setposition(x=self.start_position[0], y=new_y)