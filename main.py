from turtle import Turtle, Screen
import random

tita = Turtle()
tita.shape("turtle")

tita.color('lime')


def square(x):
    global tita
    for _ in range(4):
        tita.forward(x)
        tita.right(90)


def dashed_line():
    global tita
    for _ in range(15):
        tita.pencolor('red')
        tita.pensize(3)
        tita.pendown()
        tita.forward(10)
        tita.penup()
        tita.forward(10)


def draw_shape():
    x = 3
    while x < 9:
        arr = ["red", "tan2", "yellow", "lime"]
        c = random.choice(arr)
        for _ in range(x):
            tita.pencolor(c)
            tita.pensize(3)
            tita.forward(100)
            tita.right(360 / x)
        x += 1


def random_walk():
    arr = ["red", "tan2", "yellow", "lime"]
    directions = [0,90, 180, 270]
    tita.pensize(5)
    tita.speed(0)
    x = 0
    while x < 250:
        rd = random.choice(directions)
        col = random.choice(arr)
        tita.pencolor(col)
        tita.forward(30)
        tita.setheading(rd)
        x += 1


# dashed_line()
# square(x=100)
# draw_shape()
#random_walk()
screen = Screen()
screen.exitonclick()
