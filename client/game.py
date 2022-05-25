import sys

import pygame
import time
import random

from animation.gameAnimation import startGame
from client.enemy import spawnEnemy, SuperEnemy, SimpleEnemy
from client.control import handleBullets, handleEnemies, createEBullets, handlePowerUp, changeDificulty
from client.player import Player, Bullet
from client.powerUp import spawnPowerUp, Health, NewBullets
from client.variables import WIN, bg, END, WIDTH, HEIGHT, END_SCORE, HEALTH_FONT, SPACESHIP, \
    FPS, WHITE, BLACK, END_QUIT, FILE, ASTEROID, SUPERENEMY, ALIEN, HEART, BULLET, MAX_ENEMIES
from menu import menu

def drawEnd(WIN, player):
    width = 720
    height = 200
    Text = END.render("You Died!", 1, WHITE)
    ScoreText = END_SCORE.render(
        "Score: " + str(player.score), 1, WHITE)

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
        pygame.draw.rect(WIN, WHITE, ((WIDTH / 2 - width / 2) - 1, (HEIGHT / 2 - height / 2) - 1, width+2, height + 2))
        pygame.draw.rect(WIN, BLACK, (WIDTH/2-width/2, HEIGHT/2-height/2, width, height))
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
                menu()
        if quitb.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def redrawText(WIN, player):
    HealthText = HEALTH_FONT.render(
        "Health: " + str(player.health), 1, (255, 255, 255))
    pygame.draw.rect(WIN, (255, 255, 255), (9, 9, 202, 52))
    pygame.draw.rect(WIN, (0, 0, 0), (10, 10, 200, 50))
    WIN.blit(HealthText, (15, 15))
    ScoreText = HEALTH_FONT.render(
        "Score: " + str(player.score), 1, (255, 255, 255))
    WIN.blit(ScoreText, (15, 35))

def redrawWINdow(WIN, player, enemies, eBullets, powerUps):

    WIN.blit(bg, (0, 0))

    redrawText(WIN, player)

    WIN.blit(SPACESHIP, player.rect)

    for bullet in player.bullets:
        bullet.move()
        pygame.draw.rect(WIN, bullet.color, bullet.rect)

    for enemy in enemies:
        enemy.move()
        if type(enemy) == SuperEnemy:
            WIN.blit(SUPERENEMY, enemy.rect)
        elif type(enemy) == SimpleEnemy:
            WIN.blit(ALIEN, enemy.rect)
        else:
            WIN.blit(ASTEROID, enemy.rect)

    for eBullet in eBullets:
        eBullet.move()
        pygame.draw.rect(WIN, eBullet.color, eBullet.rect)

    for powerUp in powerUps:
        powerUp.move()
        if type(powerUp) == Health:
            WIN.blit(HEART, powerUp.rect)
        elif type(powerUp) == NewBullets:
            WIN.blit(BULLET, powerUp.rect)

    pygame.display.update()


def play():

    startGame(WIN)
    start_time = time.time()
    seconds = 0
    clock = pygame.time.Clock()
    run = True
    p = Player(50, 50, 40, 40, (0, 255, 0))
    enemies = []
    eBullets = []
    powerUps = []
    f = open(FILE, "w")

    MAX_ENEMIES = 3

    basicVelB = 10
    basicVeleB = 7
    basicVelE = 6
    basicVelSE = 5
    basicVelSupE = 3
    basicVelPUp = 3

    while run:
        f.write(str(p.x) + " " + str(p.y) + "\n")

        if seconds < int(time.time()-start_time):
            seconds = int(time.time()-start_time)
            enemies = spawnEnemy(seconds, enemies, basicVelE, basicVelSE, basicVelSupE, MAX_ENEMIES)
            powerUps = spawnPowerUp(seconds, powerUps, basicVelPUp)
            eBullets = createEBullets(enemies, eBullets, seconds, basicVeleB)
            if seconds % 15 == 0:
                basicVelB, basicVeleB, basicVelE, basicVelSE, basicVelSupE, basicVelPUp  = changeDificulty(p, basicVelB, basicVeleB, basicVelE, basicVelSE, basicVelSupE, basicVelPUp)
                MAX_ENEMIES += 1
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                f.close()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(p.bullets) < p.maxBullets:
                    bullet = Bullet((255, 0, 0), p, basicVelB)
                    p.bullets.append(bullet)
                if event.key == pygame.K_ESCAPE:
                    run = False
                    drawEnd(WIN, p)
                    f.close()

        keys = pygame.key.get_pressed()

        enemies, eBullets = handleBullets(p, p.bullets, enemies, eBullets)
        enemies = handleEnemies(p, enemies)
        powerUps = handlePowerUp(p, powerUps)

        p.move(keys)

        if p.health <= 0:
            run = False
            f.close()
            drawEnd(WIN, p)

        redrawWINdow(WIN, p, enemies, eBullets, powerUps)

    pygame.quit()
    f.close()
