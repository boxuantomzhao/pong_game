from turtle import Turtle
import random
import math

HEADINGS_deg = [45,135,225,315]
HEADINGS = [element * (math.pi/180) for element in HEADINGS_deg]

class Ball(Turtle):

    def __init__(self, initial_speed, initial_position, initial_heading):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.initial_position = initial_position
        self.setposition(initial_position)
        self.initial_speed = initial_speed
        self.initial_heading = initial_heading * math.pi / 180
        self.x_speed = self.initial_speed * math.cos(self.initial_heading)
        self.y_speed = self.initial_speed * math.sin(self.initial_heading)

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto((new_x,new_y))

    def bounce_top_bot(self):
        self.y_speed *= -1.1
        self.x_speed *= 1.1

    def bounce_left_right(self):
        self.x_speed *= -1.1
        self.y_speed *= 1.1

    def reset_position(self):
        self.setposition(self.initial_position)
        self.y_speed = random.choice([-1,1]) * self.initial_speed * math.sin(self.initial_heading)

        if self.x_speed > 0:
            self.x_speed = abs(self.initial_speed * math.cos(self.initial_heading))
        elif self.x_speed < 0:
            self.x_speed = -abs(self.initial_speed * math.cos(self.initial_heading))


