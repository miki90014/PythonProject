import pickle
import sys

import pygame
import time

from Network.network import Network
from client.player import Player
from client.variables import HEALTH_FONT, bg, SPACESHIP, END, END_SCORE, END_QUIT, WHITE, FPS, WIDTH, HEIGHT, BLACK, \
    WIN, THREE, TWO, ONE, START
#from menu import menu
from multi.secPlayer import SecPlayer, handleBullets, handleEnemies
from client.player import Bullet


class gameDate():
    def __init__(self, player, enemies, enemyBullets, powerUps, seconds):
        self.player = player
        self.enemies = enemies
        self.enemyBullets = enemyBullets
        self.powerUps = powerUps
        self.seconds = seconds
    def getPosition(self):
        return self.player.x, self.player.y
    def getScore(self):
        return self.player.score
    def getHealth(self):
        return self.player.health

def startGame():
    WIN.blit(bg, (0, 0))
    clock = pygame.time.Clock()
    for i in range(4):
        clock.tick(FPS)
        counting(i)
        time.sleep(1)
        pygame.display.update()

def counting(i):
    if(i==0):
        WIN.blit(THREE, (0, 0))
    elif i==1:
        WIN.blit(TWO, (0, 0))
    elif i==2:
        WIN.blit(ONE, (0, 0))
    else:
        WIN.blit(START, (0, 0))
    pygame.display.update()

def drawEnd(WIN, player1, player2):
    width = 720
    height =200
    if player1.score>player2.score:
        text = "Player1 won!"
    elif player2.score>player1.score:
        text = "Player2 won!"
    else:
        text = "Withdraw!"
    Text = END.render(text, 1, (255, 255, 255))
    ScoreText1 = END_SCORE.render(
        "Score Player1: " + str(player1.score), 1, WHITE)
    ScoreText2 = END_SCORE.render(
        "Score Player2: " + str(player2.score), 1, WHITE)

    Return = END_QUIT.render("Menu", 1, WHITE)
    Quit = END_QUIT.render("Exit", 1, WHITE)

    clock = pygame.time.Clock()
    run = True

    buttonw = 370
    buttonh = 50
    buttonx = WIDTH / 18
    buttony = (HEIGHT / 1.2)
    padding = 400 + buttonx

    quitb = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    quitw = pygame.Rect(buttonx - 1, buttony - 1, buttonw + 2, buttonh + 2)

    buttonx += padding
    endb = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    endw = pygame.Rect(buttonx - 1, buttony - 1, buttonw + 2, buttonh + 2)

    while run:

        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()

        WIN.blit(bg, (0, 0))
        pygame.draw.rect(WIN, (255, 255, 255), ((WIDTH / 2 - width / 2) - 1, (HEIGHT / 2 - height / 2) - 1, width+2, height + 2))
        pygame.draw.rect(WIN, (0, 0, 0), (WIDTH/2-width/2, HEIGHT/2-height/2, width, height))
        WIN.blit(Text, (WIDTH/2-width/2 +10, HEIGHT/2-height/2 + 10))
        WIN.blit(ScoreText1, (WIDTH/2- 3*width/8, HEIGHT/2-height/2+120))
        WIN.blit(ScoreText2, (WIDTH / 2 - 3*width / 8, HEIGHT / 2 - height / 2 + 160))

        pygame.draw.rect(WIN, WHITE, quitw)
        pygame.draw.rect(WIN, BLACK, quitb)
        pygame.draw.rect(WIN, WHITE, endw)
        pygame.draw.rect(WIN, BLACK, endb)

        WIN.blit(Quit, (buttonx - padding + buttonw / 2 - 63, buttony + 5))
        WIN.blit(Return, (buttonx + buttonw / 2 - 63, buttony + 5))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if endb.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                #menu()
        if quitb.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def redrawText(WIN, player1, player2):
    HealthText1 = HEALTH_FONT.render(
        "Health Player1: " + str(player1.health), 1, (255, 255, 255))
    HealthText2 = HEALTH_FONT.render(
        "Health Player2: " + str(player2.health), 1, (255, 255, 255))
    pygame.draw.rect(WIN, (255, 255, 255), (9, 9, 282, 102))
    pygame.draw.rect(WIN, (0, 0, 0), (10, 10, 280, 100))
    WIN.blit(HealthText1, (15, 15))
    #WIN.blit()
    ScoreText1 = HEALTH_FONT.render(
        "Score Player1: " + str(player1.score), 1, (255, 255, 255))
    ScoreText2 = HEALTH_FONT.render(
        "Score Player2: " + str(player2.score), 1, (255, 255, 255))
    WIN.blit(ScoreText1, (15, 35))
    WIN.blit(HealthText2, (15, 55))
    WIN.blit(ScoreText2, (15, 75))

def redrawWINdow(WIN, player1, player2, enemies, eBullets, powerUps):

    WIN.blit(bg, (0, 0))

    redrawText(WIN, player1, player2)

    #pygame.draw.rect(WIN, player.color, player.rect)
    WIN.blit(SPACESHIP, player1.rect)
    WIN.blit(SPACESHIP, player2.rect)

    for bullet in player1.bullets:
        bullet.move()
        pygame.draw.rect(WIN, bullet.color, bullet.rect)

    for bullet in player2.bullets:
        bullet.move()
        pygame.draw.rect(WIN, bullet.color, bullet.rect)

    for enemy in enemies:
        enemy.move()
        pygame.draw.rect(WIN, enemy.color, enemy.rect)

    for eBullet in eBullets:
        eBullet.move()
        pygame.draw.rect(WIN, eBullet.color, eBullet.rect)

    for powerUp in powerUps:
        powerUp.move()
        pygame.draw.rect(WIN, powerUp.color, powerUp.rect)

    pygame.display.update()

def readPos(string):
    print(string)
    string = str(string).split(",")
    print(string)
    return int(string[0]), int(string[1])

def makePos(tup):
    return (str(tup[0])+", "+str(tup[1]))




def play():
    startGame()
    n = Network()


    print(n.getPos())
    startPos = readPos(n.getPos())

    global MAX_ENEMIES
    start_time = time.time()
    seconds = 0
    clock=pygame.time.Clock()
    run = True
    p1 = Player(startPos[0],startPos[1],40,40,(0,255,0))
    p2 = Player(0, 0,40,40,(0,255,0)) #SecPlayer(50,50,40,40,(0,255,170))
    enemies = []
    eBullets = []
    powerUps = []
    while run:

        p2Pos = readPos(n.send(makePos((p1.x, p1.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.upadte()


        if seconds< (int)(time.time()-start_time):
            seconds = (int)(time.time()-start_time)
            #enemies = spawnEnemy(seconds, enemies)
            #powerUps = spawnPowerUp(seconds, powerUps)
            #eBullets = createEBullets(enemies, eBullets, seconds)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(p1.bullets) < p1.maxBullets:
                    bullet = Bullet((0,0,0),p1, WIN)
                    p1.bullets.append(bullet)
                if event.key == pygame.K_ESCAPE:
                    run = False
                    drawEnd(WIN, p1, p2)
        keys = pygame.key.get_pressed()
        enemies, eBullets = handleBullets(p1, p2, p1.bullets, p2.bullets, enemies, eBullets)
        enemies = handleEnemies(p1, p2, enemies)
        #powerUps = handlePowerUp(p, powerUps)
        p1.move(keys)
        p2.move(keys)

        if p1.health<=0 or p2.health<=0:
            run = False
            drawEnd(WIN, p1, p2)

        redrawWINdow(WIN, p1, p2, enemies, eBullets, powerUps)

        variable = gameDate(p1, enemies, eBullets, powerUps, seconds)
        data_string = pickle.dumps(variable)
        n.send(data_string)

    pygame.quit()