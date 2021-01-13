import turtle
from random import randrange

skk = turtle.Turtle()
turtle.colormode(255)
skk.speed(1)
skk.color("green")
skk.left(90)
ln = 50
skk.forward(ln)
par = skk.position()


def dud(ln,parr,neg = False ):
    newlen = ln/2

    newPos = parr
    if ln > 6.24:

        if neg:
            skk.left(-30)
            turn = 30
        else:
            skk.left(30)
            turn = -30

        skk.forward(ln)
        newPos = skk.position()

        dud(newlen, newPos, False)
        skk.up()
        skk.goto(parr)
        skk.left(turn)
        skk.down()
        dud(newlen, newPos, True)



dud(ln,par,False)


def shape():







    pass













skk.hideturtle()
turtle.done()
