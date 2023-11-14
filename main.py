from turtle import Turtle, Screen

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

        for _ in range(x):
            tita.pensize(3)
            tita.forward(100)
            tita.right(360 / x)
        x += 1


# dashed_line()
# square(x=100)
# draw_shape()
screen = Screen()
screen.exitonclick()
