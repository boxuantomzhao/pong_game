#Importing the necessary things
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import random
import time


# -------------------------- Initializing canvas
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# -------------------------- Create objects
# centre reference
center = Turtle()
center.hideturtle()
center.color("white")
# center.setposition(x=-300, y = 0)
# center.forward(600)
center.penup()
center.setposition((0,275))
center.write(arg="< Score >", move=False, align="center", font=("arial",14,"normal"))

# Asking for some user input
welcome = screen.textinput(title="Welcome to Pong", prompt="Left side paddle is controlled by w-s, "
                                                           "right side paddle is controlled by up-down key.\n"
                                                           "Single key press only, don't press and hold. \n"
                                                "If u miss the ball, opponent scores, and first to 3 point wins. \n"
                                                           "The ball gets faster after each bounce. \n"
                                                           "If you are ready, click 'OK' ")

handicap = screen.numinput(title="Handicap Factor",
                           prompt="Input a factor from 1 to 5 (1 is a fair game, 5 strongly favors left player)",
                           default=1, minval=1, maxval=5)
paddle_size1 = 5
paddle_size2 = handicap*paddle_size1
paddle1_collision_detection = handicap*50
paddle2_collision_detection = handicap*50

ball_speed = screen.numinput(title="Initial Ball Speed", prompt="Input a num from 2 to 5",default=2, minval=2,maxval=5)
# some collision detection parameter needs to be scaled based on paddle length

ball = Ball(initial_speed=float(ball_speed), initial_position=(0, 0),initial_heading=random.choice([45,135,225,315]))
# ball = Ball(initial_speed=5, initial_position=(0, 0),initial_heading=random.choice([45,135,225,315]))
paddle1 = Paddle(paddle_len=float(paddle_size1), start_position=(350,0),speed=40)
paddle2 = Paddle(paddle_len=float(paddle_size2), start_position=(-350,0),speed=40)
score1 = ScoreBoard(position=(100, 275), user_name="Right")
score2 = ScoreBoard(position=(-100, 275), user_name="Left")

# --------------------- Screen commands, listen for key strokes
screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

# --------------------- Main program
game_on = True

while game_on:
    screen.update()
    time.sleep(0.001)
    score1.show_score()
    score2.show_score()
    ball.move()

    # Detect collision with top/bottom wall
    if abs(ball.ycor()) > 290:
        ball.bounce_top_bot()

    # Detect collision with paddles
    if ball.distance(paddle1) < paddle1_collision_detection and ball.xcor() > 340 \
            or ball.distance(paddle2) < paddle2_collision_detection and ball.xcor() < -340:
        ball.bounce_left_right()

    # Detect if right paddle misses (paddle 1)
    if ball.xcor() > 390:
        ball.bounce_left_right()
        #left paddle scores
        score2.add_score()
        ball.reset_position()

    # Detect if left paddle misses (paddle 2)
    if ball.xcor() < -390:
        ball.bounce_left_right()
        #right paddle scores
        score1.add_score()
        ball.reset_position()

    if score1.score > 2:
        score1.game_over()

        game_on = False
    elif score2.score > 2:
        score2.game_over()
        game_on = False


screen.exitonclick()