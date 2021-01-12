import turtle
from random import randrange

skk = turtle.Turtle()
turtle.colormode(255)
skk.speed(10)


def shape(ln):
    skk.down()
    skk.forward(ln)
    for dud in range(4):

        skk.right(72)
        skk.forward(ln/2)
        skk.backward(ln/2)

    skk.right(72)
    if ln > 10:
        shape(ln/2)


for x in range(6):

    skk.up()
    skk.home()
    skk.left((x+1)*60)
    shape(150)

skk.hideturtle()
turtle.done()
