import pygame

pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500
FPS = 80

WHITE=(255,255,255)
BLACK=(0,0,0)

bg = pygame.image.load("images\\background.jpg")
#bg = pygame.transform.scale(bg, (900,500))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")
#WIN.fill((255, 255, 255))

ONE = pygame.image.load("images\\backgroundONE.jpg")
#ONE = pygame.transform.scale(ONE, (900,500))
TWO = pygame.image.load("images\\backgroundTWO.jpg")
#TWO = pygame.transform.scale(TWO, (900,500))
THREE = pygame.image.load("images\\backgroundTHREE.jpg")
#THREE = pygame.transform.scale(THREE, (900,500))
START = pygame.image.load("images\\backgroundSTART.jpg")
#START = pygame.transform.scale(START, (900,500))

SPACESHIP = pygame.image.load("images\\spaceship.png")
SPACESHIP = pygame.transform.scale(SPACESHIP, (40,40))

HEALTH_FONT = pygame.font.Font('font\\game.ttf', 20)
SCORE_FONT = pygame.font.Font('font\\game.ttf', 20)

END = pygame.font.Font('font\\game.ttf', 100)
END_SCORE = pygame.font.Font('font\\game.ttf', 40)

END_QUIT = pygame.font.Font('font\\game.ttf', 40)

MAX_ENEMIES = 3
enemies = []