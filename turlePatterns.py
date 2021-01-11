import turtle
from random import randrange

skk = turtle.Turtle()
turtle.colormode(255)
skk.speed(100)

for x in range(4):
    for i in range(40):
        randRed = randrange(0, 200)
        randBlue = randrange(0, 200)
        randGreen = randrange(0, 200)

        #skk.pencolor((randRed, randBlue, randGreen))

        if i % 3 == 1:
            skk.color((randRed,100,100))

        elif i % 3 == 2:
            skk.color((100,randBlue,100))

        else:
            skk.color((100,100,randGreen))

        skk.circle((x*50)+50)
        skk.left(9)


skk.hideturtle()
turtle.done()
