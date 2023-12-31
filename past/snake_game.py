import random
from turtle import Screen, Turtle
from time import sleep
import os

display_surface = Screen()
display_surface.bgcolor("black")
display_surface.setup(600, 600)
display_surface.title("~~Snake Game~~")
display_surface.tracer(False)


def create_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_position(object):
    x = random.randint(-270, 270)
    y = random.randint(-270, 230)
    object.goto(x, y)


def move_snake():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)


poison_apple = create_turtle("circle", "darkgreen")
change_position(poison_apple)


display_surface.listen()
display_surface.onkeypress(go_up, "Up")
display_surface.onkeypress(go_down, "Down")
display_surface.onkeypress(go_left, "Left")
display_surface.onkeypress(go_right, "Right")

snake_tails = []
score = 0

if os.path.exists("score.txt"):
    with open("score.txt","r") as f:

        high_score = int(f.read())
else:
    high_score = 0

scoreboard = create_turtle("square", "white")
scoreboard.goto(0, 260)
scoreboard.ht()

def on_close():
    with open("score.txt","w") as file:
        file.write(str(high_score))
    global running
    running = False


root = display_surface._root
root.protocol("WM_DELETE_WINDOW", on_close)


running = True
while running:
    scoreboard.clear()
    scoreboard.write(f"Score: {score}, HighScore: {high_score}", font=(
        "arial", 24), align="center")
    display_surface.update()
    # Check when snake eats the food
    if snake_head.distance(snake_food) < 20:
        change_position(snake_food)
        new_tail = create_turtle("square", "green")
        snake_tails.append(new_tail)
        score += 1

    
    if snake_head.distance(poison_apple) < 20:
        change_position(poison_apple)
        score -= 1
        if len(snake_tails) > 0:
            snake_tails[-1].ht()
            del snake_tails[-1]
    if score < 0:
        score = 0
        snake_head.home()
        snake_head.direction = ""
        for tail in snake_tails:
            tail.ht()

        snake_tails = []

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        if score > high_score:
            high_score = score
        score = 0
        snake_head.home()
        snake_head.direction = ""
        for tail in snake_tails:
            tail.ht()

        snake_tails = []

    for i in range(len(snake_tails)-1, 0, -1):
        x = snake_tails[i-1].xcor()
        y = snake_tails[i-1].ycor()
        snake_tails[i].goto(x, y)

    if len(snake_tails) > 0:
        snake_tails[0].goto(snake_head.xcor(), snake_head.ycor())

    move_snake()
    for tail in snake_tails:
        if tail.distance(snake_head)<20:
            if score > high_score:
                high_score = score
            score = 0
            snake_head.home()
            snake_head.direction = ""
            for tail in snake_tails:
                tail.ht()

            snake_tails = []



    sleep(0.2)
