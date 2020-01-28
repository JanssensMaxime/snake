import turtle
import time
import random


#delay window update
delay = 0.15

#screen setup
window = turtle.Screen()
window.title("Snake")
window.bgcolor("white")
window.setup(width = 600, height = 600)
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
food.goto(0, 100)

#create body of snake
body_parts = []

#BASIC TURTLE SHAPES ARE 20X20 PIXELS
#nbPixels used to move
moving_range = 20

#moving snake
def move_snake():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + moving_range)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - moving_range)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - moving_range)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + moving_range)



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


def move_body():
    #move body of snake
    #moving last part first => reverse order
    for index in range(len(body_parts)-1, 0, -1):
        x = body_parts[index-1].xcor()
        y = body_parts[index-1].ycor()
        body_parts[index].goto(x, y)
        
    #move part 0 to last head position
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)

def collisions():
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #hide body_parts
        for part in body_parts:
            part.goto(1000, 1000)

        #clear body_parts
        body_parts.clear()

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

    #check for border collision
    if head.xcor() >  (turtle.window_width() /2) -10 or head.xcor() < -(turtle.window_width() /2) +10 or head.ycor() > (turtle.window_width() /2) -10 or head.ycor() < -(turtle.window_width() /2) +10:
        collisions()
        
    #collision with food
    if head.distance(food) < 20:
        create_food()

        new_body_part = turtle.Turtle()
        new_body_part.speed(0)
        new_body_part.shape("square")
        new_body_part.color("lightgreen")
        new_body_part.penup()
        body_parts.append(new_body_part)

    move_body()

    move_snake()

    #check for body collision
    for part in body_parts:
        if part.distance(head) < 20:
            collisions()

    time.sleep(delay)


window.mainloop()