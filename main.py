import pygame
import numpy as np
from random import randrange
from sys import exit

"""
calc mid
calc max
calc min
gen pattern
- start smol

"""


class Pattern:

    def __init__(self):
        self.pattern = {}

        self.gameName = 'Pattern renders'
        self.gameRes = (2560, 1440)#(1000, 1000)#
        self.gameScreen = pygame.display.set_mode(self.gameRes)

        self.taskBarSize = 60

        self.midX = self.gameRes[0] / 2
        self.midY = self.gameRes[1] / 2
        self.min = 0
        self.max = self.gameRes[0]

        self.running = True

    def render(self):
        pygame.init()
        pygame.display.set_caption(self.gameName)
        self.gameScreen.fill((0, 0, 0))
        pygame.draw.rect(self.gameScreen, (0, 0, 0), pygame.Rect(0, 0, 640, 640), 1)

        self.breakPoints(5)

        pygame.image.save(self.gameScreen, "screenshot.jpg")

        while self.running:

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    exit(0)

            pygame.display.update()

    def breakPoints(self, perSide):

        breakPoints = []
        scrSizeX = self.gameRes[0]
        scrSizeY = self.gameRes[1]-self.taskBarSize

        for poNum in range(perSide):

            pointCordX = int((poNum + 1) * (scrSizeX / (perSide + 1)))
            pointCordY = int((poNum + 1) * (scrSizeY / (perSide + 1)))

            breakPoints.append((pointCordX, 0))
            breakPoints.append((pointCordX, scrSizeY))
            breakPoints.append((0, pointCordY))
            breakPoints.append((scrSizeX, pointCordY))

        breakPoints.append((0, 0))
        breakPoints.append((scrSizeX, 0))
        breakPoints.append((0, scrSizeY))
        breakPoints.append((scrSizeX, scrSizeY))

        print(breakPoints)
        self.allPoints(breakPoints)

    def allPoints(self, pointList):
        toggleBool = False
        if len(pointList) == 0:
            return True

        mainPoint = pointList[0]
        lst = pointList[1:]

        for lstLen in range(len(lst)):
            if toggleBool or mainPoint[0] != lst[lstLen][0] and mainPoint[1] != lst[lstLen][1]:
                print(lst[lstLen])
                randRed = randrange(0, 200)
                randBlue = randrange(0, 200)
                randGreen = randrange(0, 200)

                pygame.draw.line(self.gameScreen, (randRed, randBlue, 225), mainPoint, lst[lstLen], 3)

        self.allPoints(lst)


Pattern().render()
