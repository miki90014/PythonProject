import pygame
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.font.init()
#pygame.mixer.init()

WIDTH = 900
HEIGHT = 500
FPS = 80

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (249, 215, 28)
ORANGEYELLOW = (255, 172, 0)

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = PATH.replace("client", "")


FILE = PATH+"temp/lastKeyListening"
INST = PATH+"txt/instructions"

bg = pygame.image.load(PATH+"images/background.jpg")
bg = pygame.transform.scale(bg, (900, 500))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")
#WIN.fill((255, 255, 255))

START = pygame.image.load(PATH+"images/backgroundSTART.jpg")
START = pygame.transform.scale(START, (900,500))

SPACESHIP = pygame.image.load(PATH+"images/spaceship.png")
SPACESHIP = pygame.transform.scale(SPACESHIP, (40,40))

ASTEROID = pygame.image.load(PATH+"images/asteroid.png")
ASTEROID = pygame.transform.scale(ASTEROID, (50,50))

SUPERENEMY = pygame.image.load(PATH+"images/superEnemy.png")
SUPERENEMY = pygame.transform.scale(SUPERENEMY, (50,50))

ALIEN = pygame.image.load(PATH+"images/alien.png")
ALIEN = pygame.transform.scale(ALIEN, (50,50))

HEART = pygame.image.load(PATH+"images/heart.png")
HEART = pygame.transform.scale(HEART, (50,50))

BULLET = pygame.image.load(PATH+"images/bullet.png")
BULLET = pygame.transform.scale(BULLET, (50,50))

#LOSE_HEALTH = pygame.mixer.Sound(PATH+"sound\\health.mp3")
#START_UP = pygame.mixer.Sound(PATH+"sound\\startup.mp3")
#POWERUP = pygame.mixer.Sound(PATH+"sound\\powerup.mp3")

HEALTH_FONT = pygame.font.Font(PATH+'font/game.ttf', 20)
SCORE_FONT = pygame.font.Font(PATH+'font/game.ttf', 20)

INSTRUCTION_FONT = pygame.font.Font(PATH+'font/game.ttf', 15)

END = pygame.font.Font(PATH+'font/game.ttf', 100)
END_SCORE = pygame.font.Font(PATH+'font/game.ttf', 40)

END_QUIT = pygame.font.Font(PATH+'font/game.ttf', 40)

TITTLE_FONT = pygame.font.Font(PATH+'font/game.ttf', 100)
OPTION_FONT = pygame.font.Font(PATH+'font/game.ttf', 40)

MAX_ENEMIES = 3
enemies = []
VEL = 1.1