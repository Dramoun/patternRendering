import turtle
from random import randrange

skk = turtle.Turtle()
turtle.colormode(255)
skk.speed(100000)
skk.left(90)


def binaryTree():
    wd = 15
    skk.up()
    skk.goto(0, -400)
    skk.down()
    ln = 200

    def dud(ln, wd):

        if ln > 10:
            if ln > 70:
                skk.color("brown")
            else:
                skk.color("green")

            skk.width(wd*0.8)
            newWd = wd*0.8

            skk.forward(ln)

            skk.left(45)

            dud(ln*0.75,newWd)

            skk.right(90)

            dud(ln*0.75,newWd)
            skk.left(45)
            skk.up()
            skk.forward(-ln)
            skk.down()

    dud(ln,wd)

binaryTree()

skk.hideturtle()
turtle.done()
