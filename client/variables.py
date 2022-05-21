import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500
FPS = 80

WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW = (249, 215, 28)
ORANGEYELLOW = (255, 172, 0)

PATH=os.path.dirname(os.path.abspath(__file__))
PATH=PATH.replace("client", "")

FILE = PATH+"temp\\lastKeyListening"
INST = PATH+"txt\\instructions"

bg = pygame.image.load(PATH+"images\\background.jpg")
#bg = pygame.transform.scale(bg, (900,500))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")
#WIN.fill((255, 255, 255))

ONE = pygame.image.load(PATH+"images\\backgroundONE.jpg")
#ONE = pygame.transform.scale(ONE, (900,500))
TWO = pygame.image.load(PATH+"images\\backgroundTWO.jpg")
#TWO = pygame.transform.scale(TWO, (900,500))
THREE = pygame.image.load(PATH+"images\\backgroundTHREE.jpg")
#THREE = pygame.transform.scale(THREE, (900,500))
START = pygame.image.load(PATH+"images\\backgroundSTART.jpg")
#START = pygame.transform.scale(START, (900,500))

SPACESHIP = pygame.image.load(PATH+"images\\spaceship.png")
SPACESHIP = pygame.transform.scale(SPACESHIP, (40,40))

HEALTH_FONT = pygame.font.Font(PATH+'font\\game.ttf', 20)
SCORE_FONT = pygame.font.Font(PATH+'font\\game.ttf', 20)

INSTRUCTION_FONT = pygame.font.Font(PATH+'font\\game.ttf', 15)

END = pygame.font.Font(PATH+'font\\game.ttf', 100)
END_SCORE = pygame.font.Font(PATH+'font\\game.ttf', 40)

END_QUIT = pygame.font.Font(PATH+'font\\game.ttf', 40)

MAX_ENEMIES = 3
enemies = []