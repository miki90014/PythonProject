import sys
from types import NoneType

import pygame
import time
import random

from Client.Enemy import spawnEnemy
from Client.control import handleBullets, handleEnemies
from Client.player import Player, Bullet
from Client.variables import WIN, bg, THREE, TWO, ONE, START, END, WIDTH, HEIGHT, END_SCORE, HEALTH_FONT, SPACESHIP, \
    FPS, WHITE, BLACK, END_QUIT
from menu import menu


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

def drawEnd(WIN, player):
    width = 720
    height =200
    Text = END.render("You Died!", 1, (255, 255, 255))
    ScoreText = END_SCORE.render(
        "Score: " + str(player.score), 1, (255, 255, 255))

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
        WIN.blit(ScoreText, (WIDTH/2-width/8, HEIGHT/2-height/2+150))

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
                print("Sth's gone wrong")
                menu()
        if quitb.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def redrawWINdow(WIN, player, enemies):

    WIN.blit(bg, (0, 0))

    HealthText = HEALTH_FONT.render(
        "Health: " + str(player.health), 1, (255, 255, 255))
    pygame.draw.rect(WIN, (255, 255, 255), (9, 9, 202, 52))
    pygame.draw.rect(WIN, (0, 0, 0), (10, 10, 200, 50))
    WIN.blit(HealthText, (15, 15))
    ScoreText = HEALTH_FONT.render(
        "Score: " + str(player.score), 1, (255, 255, 255))
    WIN.blit(ScoreText, (15, 35))

    #pygame.draw.rect(WIN, player.color, player.rect)
    WIN.blit(SPACESHIP, player.rect)

    for bullet in player.bullets:
        bullet.move()
        pygame.draw.rect(WIN, bullet.color, bullet.rect)
    print(len(enemies))
    for enemy in enemies:
        enemy.move()
        pygame.draw.rect(WIN, enemy.color, enemy.rect)
    pygame.display.update()

def play():
    startGame()
    global MAX_ENEMIES
    start_time = time.time()
    seconds = 0
    clock=pygame.time.Clock()
    run = True
    p = Player(50,50,40,40,(0,255,0))
    enemies = []
    while run:
        if seconds< (int)(time.time()-start_time):
            seconds = (int)(time.time()-start_time)
            enemies = spawnEnemy(seconds, enemies)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(p.bullets) < p.maxBullets:
                    bullet = Bullet((0,0,0),p, WIN)
                    p.bullets.append(bullet)
        keys = pygame.key.get_pressed()
        enemies = handleBullets(p, p.bullets, enemies)
        enemies = handleEnemies(p, enemies)
        p.move(keys)

        if p.health==0:
            run = False
            drawEnd(WIN, p)

        redrawWINdow(WIN, p, enemies)
    pygame.quit()