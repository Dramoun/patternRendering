import turtle
from random import randrange

skk = turtle.Turtle()
turtle.colormode(255)
skk.speed(1000)
skk.screen.bgcolor((150,150,150))

for x in range(8):
    for i in range(10):

        skk.color((250-(25*(i+1)), 0, 0))
        skk.down()
        skk.forward((i+1)*18)
        skk.right(30)

    skk.up()
    skk.home()
    skk.right((x+1)*45)


skk.up()
skk.home()

for x in range(8):
    for i in range(10):
        skk.color((250-(25*(i+1)), 0, 0))

        skk.down()
        skk.forward((i+1)*18)
        skk.left(30)

    skk.up()
    skk.home()
    skk.left((x+1)*45)

skk.hideturtle()
turtle.done()
