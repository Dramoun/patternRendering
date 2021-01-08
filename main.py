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
        self.gameRes = (1000, 1000)
        self.gameScreen = pygame.display.set_mode(self.gameRes)

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

        self.shape(7)

        while self.running:

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    exit(0)

            pygame.display.update()

    def shape(self, perSide):

        breakPoints = []
        scrSize = self.gameRes[0]

        for poNum in range(perSide):

            pointCord = int((poNum + 1) * (scrSize / (perSide + 1)))
            breakPoints.append((pointCord, 0))
            breakPoints.append((pointCord, scrSize))
            breakPoints.append((0, pointCord))
            breakPoints.append((scrSize, pointCord))

        breakPoints.append((0, 0))
        breakPoints.append((scrSize, 0))
        breakPoints.append((0, scrSize))
        breakPoints.append((scrSize, scrSize))

        self.allPoints(breakPoints)

    def allPoints(self, pointList):

        if len(pointList) == 0:
            return True

        mainPoint = pointList[0]
        lst = pointList[1:]

        for lstLen in range(len(lst)):

            randRed = randrange(0, 255)
            randBlue = randrange(50, 150)
            randGreen = randrange(0, 255)

            pygame.draw.line(self.gameScreen, (randRed, randBlue, 255), mainPoint, lst[lstLen], 1)

        self.allPoints(lst)


Pattern().render()
