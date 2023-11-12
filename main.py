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


# dashed_line()
# square(x=100)

screen = Screen()
screen.exitonclick()
