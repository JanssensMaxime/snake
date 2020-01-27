import turtle
import time
import random

#delay window update
delay = 0.15

#screen setup
window = turtle.Screen()
window.title("Snake")
window.bgcolor("white")
window.setup(width=600, height=600)
window.tracer(0) #draw true/false

#TURTLES

#create head of snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("darkgreen")
head.penup()
head.goto(0,0)
head.direction = "stop"

#create food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#create body of snake
bodyParts = []

#BASIC TURTLE SHAPES ARE 20X20 PIXELS
#nbPixels used to move
moving_range = 20

#moving snake
def move_snake():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+moving_range)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-moving_range)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-moving_range)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+moving_range)



#moving functions
def move_up():
    head.direction = "up"

def move_down():
    head.direction = "down"

def move_left():
    head.direction = "left"

def move_right():
    head.direction = "right"

#create food at random location
def create_food():
    x = random.randint(-(turtle.window_width() /2) +10, (turtle.window_width() /2) -10)
    y = random.randint(-(turtle.window_width() /2) +10, (turtle.window_width() /2) -10)
    food.goto(x, y)


#keyboard bindings with moving functions
window.listen()
window.onkeypress(move_up, "z")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "q")
window.onkeypress(move_right, "d")


#running game
while True:
    #update window for changes
    window.update()

    #collision with food
    if head.distance(food) < 20:
        create_food()

        new_bodyPart = turtle.Turtle()
        new_bodyPart.speed(0)
        new_bodyPart.shape("square")
        new_bodyPart.color("lightgreen")
        

    move_snake()

    time.sleep(delay)


window.mainloop()