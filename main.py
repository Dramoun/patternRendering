import pygame
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
        self.gameRes = (640, 640)
        self.gameScreen = pygame.display.set_mode(self.gameRes)

        self.midX = self.gameRes[0] / 2
        self.midY = self.gameRes[1] / 2
        self.min = 0
        self.max = self.gameRes[0]

        self.running = True

    def render(self):
        pygame.init()
        pygame.display.set_caption(self.gameName)
        self.gameScreen.fill((255, 255, 255))

        self.shape()

        while self.running:

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    exit(0)

            pygame.display.update()

    def shape(self):
        pygame.draw.line(self.gameScreen, (50, 50, 50), (0, 0), (640, 640), 3)
        pygame.draw.line(self.gameScreen, (50, 50, 50), (640, 0), (0, 640), 3)
        pygame.draw.rect(self.gameScreen, (255, 0, 0), pygame.Rect(318, 318, 4, 4))


Pattern().render()
