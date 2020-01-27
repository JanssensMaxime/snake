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

#BASIC TURTLE SHAPES ARE 20X20 PIXELS
#nbPixels used to move
movingRange = 20

#moving snake
def moveSnake():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+movingRange)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-movingRange)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-movingRange)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+movingRange)



#moving functions
def moveUp():
    head.direction = "up"

def moveDown():
    head.direction = "down"

def moveLeft():
    head.direction = "left"

def moveRight():
    head.direction = "right"

#keyboard bindings with moving functions
window.listen()
window.onkeypress(moveUp, "z")
window.onkeypress(moveDown, "s")
window.onkeypress(moveLeft, "q")
window.onkeypress(moveRight, "d")


#running game
while True:
    #update window for changes
    window.update()

    if head.distance(food) < 20:
        x = random.randint(-turtle.window_width()/2, turtle.window_width()/2)
        y = random.randint(-turtle.window_width()/2, turtle.window_width()/2)
        food.goto(x, y)

    moveSnake()

    time.sleep(delay)


window.mainloop()