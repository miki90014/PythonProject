import pygame

from client.variables import START, START_UP
import time


def startGame(WIN):
    WIN.blit(START, (0, 0))
    while True:
        pygame.display.update()
        clock = pygame.time.Clock()
        time.sleep(1)
        START_UP.play()
        break