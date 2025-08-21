import turtle
import time
import random


speed = 20
delay = 0.05

foods = []
new_foods = []
food_speed = 15

score = 0
high_score = 0





# screen set up:

win = turtle.Screen()
win.title("TURTLE GAME")
win.setup(width= 600,height= 600)
win.bgcolor("black")
win.tracer(0)

# turtle head:

shape = turtle.Turtle()
shape.color("green")
shape.shape("turtle")
shape.penup()
shape.setheading(90)
shape.goto(0,-260)
shape.direction = "stop"

scoring = turtle.Turtle()
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,270)
scoring.write("SCORE =  HIGH SCORE =  ",align="center",font=("courier",15,"normal"))



def update_score():

    scoring.clear()
    scoring.write("SCORE = {} HIGH SCORE = {}".format(score,high_score),align="center",font=("courier",15,"normal"))

def create_food():

    for item in range(3):
        food = turtle.Turtle()
        food.color("green")
        food.shape("circle")
        food.penup()
        reset_food(food)
        foods.append(food)
    

        new_food = turtle.Turtle()
        new_food.color("red")
        new_food.shape("circle")
        new_food.penup()
        reset_food(new_food)
        new_foods.append(new_food)

    
def reset_food(food):

    x = random.randint(-win.window_width() // 2 + 30,win.window_width() // 2 - 30)
    y = random.randint(win.window_height()// 2,win.window_height() // 2 + 100)
    food.goto(x,y)


def move_food():
    global score,high_score

    for food in foods:
        food.sety(food.ycor() - food_speed)

        if shape.distance(food) < 30:
            score += 10
            update_score()
            reset_food(food)

            if score > high_score:
                high_score = score
                update_score()

        if food.ycor() <= (-win.window_height() // 2):
            reset_food(food)


    for new_food in new_foods:
        new_food.sety(new_food.ycor() - food_speed)

        if shape.distance(new_food) < 30:
            score = 0
            update_score()
            reset_food(new_food)

        if new_food.ycor() <= (-win.window_height() // 2):
            reset_food(new_food)



def move_left():
    shape.direction = "left"

def move_right():
    shape.direction = "right"



def move_shape():

    if shape.direction == "left":
        shape.setx(shape.xcor() - speed)
    
    if shape.direction == "right":
        shape.setx(shape.xcor() + speed)


    if shape.xcor() < (-win.window_width() // 2 + 30 ):
        shape.setx(-win.window_width() // 2 + 30)

    if shape.xcor() > (win.window_width() // 2 - 30 ):
        shape.setx(win.window_width() // 2 - 30)
    



win.listen()   # key binding:

win.onkeypress(move_left,"Left")
win.onkeypress(move_right,"Right")



create_food()

# MAIN LOOP OF GAME:
while True:
    win.update()
    move_food()
    move_shape()

    time.sleep(delay)


win.mainloop()