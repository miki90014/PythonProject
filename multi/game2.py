import sys
import time

import pygame

from Network.network import Network
from Server.variablesServer import gameDate, PlayerData, BulletsData
from client.player import Player, Bullet
from client.variables import FPS, WIN, SPACESHIP, bg, HEALTH_FONT


def redrawText(WIN, player1, player2):
    HealthText1 = HEALTH_FONT.render(
        "Your Health: " + str(player1.health), 1, (255, 255, 255))
    HealthText2 = HEALTH_FONT.render(
        "Health Player2: " + str(player2.health), 1, (255, 255, 255))
    pygame.draw.rect(WIN, (255, 255, 255), (9, 9, 282, 102))
    pygame.draw.rect(WIN, (0, 0, 0), (10, 10, 280, 100))
    WIN.blit(HealthText1, (15, 15))
    #WIN.blit()
    ScoreText1 = HEALTH_FONT.render(
        "Your Score: " + str(player1.score), 1, (255, 255, 255))
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

def packToData(player, enemies, enemyBullets, powerUps, playerNumber, end):
    global players
    newBullets = []
    for bullet in player.bullets:
        newBullets.append(BulletsData(bullet.x, bullet.y, bullet.color, bullet.player))
    newPlayerDate = PlayerData(player.x, player.y, player.color, player.health, player.score, player.maxBullets, newBullets)
    return gameDate(newPlayerDate, enemies, enemyBullets, powerUps, playerNumber, end)

def unpackData(data):

    newPlayer = Player(data.player.x, data.player.y, 40, 40, data.player.color)
    for bullet in data.player.bullets:
        newPlayer.bullets.append(Bullet(bullet.x, bullet.y, bullet.color, bullet.newPlayer, WIN))

    return newPlayer, data.enemies, data.enemyBullets, data.powerUps, data.end


def play():
    n = Network()
    playerNumber =int(n.number)
    print("You are player numer: "+ str(playerNumber))
    players = []
    enemies = []
    eBullets = []
    powerUps = []
    players.append(Player(50,50,40,40,(0,255,0)))
    players.append(Player(100, 50, 40, 40, (255, 0, 255)))
    pygame.time.delay(3000)
    global MAX_ENEMIES
    start_time = time.time()
    seconds = 0
    clock=pygame.time.Clock()
    run = True
    while run:

        if seconds< (int)(time.time()-start_time):
            seconds = (int)(time.time()-start_time)
            #enemies = spawnEnemy(seconds, enemies)
            #powerUps = spawnPowerUp(seconds, powerUps)
            #eBullets = createEBullets(enemies, eBullets, seconds)
        clock.tick(120)

        pygame.time.delay(50)

        try:
            cos = n.send(packToData(players[playerNumber], enemies, eBullets, powerUps, playerNumber, False))
            print(type(cos))
            #players[(playerNumber + 1) % 2], enemies, eBullets, powerUps = unpackData(
             #   n.send(packToData(players[playerNumber], enemies, eBullets, powerUps, playerNumber, False)))
            #redrawWINdow(WIN, players[playerNumber], players[(playerNumber + 1) % 2], enemies, eBullets, powerUps)
        except:
            run = False
            print("Couldn't get game")
            break

        players[(playerNumber + 1) % 2], enemies, eBullets, powerUps, end = unpackData(cos)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(players[playerNumber].bullets) < players[playerNumber].maxBullets:
                    bullet = Bullet((0,0,0),players[playerNumber], WIN)
                    players[playerNumber].bullets.append(bullet)
                if event.key == pygame.K_ESCAPE:
                    run = False
                    players[(playerNumber + 1) % 2], enemies, eBullets, powerUps = unpackData(n.send(packToData(players[playerNumber], enemies, eBullets, powerUps, playerNumber, True)))
                    pygame.quit()
                    sys.exit()
                    #drawEnd(WIN, p1, p2)
        keys = pygame.key.get_pressed()
        #enemies, eBullets = handleBullets(p1, p2, p1.bullets, p2.bullets, enemies, eBullets)
        #enemies = handleEnemies(p1, p2, enemies)
        #powerUps = handlePowerUp(p, powerUps)
        players[playerNumber].move(keys)

        if players[playerNumber].health<=0 or players[playerNumber].health<=0:
            run = False
            #players[(playerNumber + 1) % 2], enemies, eBullets, powerUps = unpackData(n.send(packToData(players[playerNumber], enemies, eBullets, powerUps, playerNumber, True)))
            pygame.quit()
            sys.exit()
            #drawEnd(WIN, p1, p2)

        #players[(playerNumber + 1) % 2], enemies, eBullets, powerUps = unpackData(n.send(packToData(players[playerNumber], enemies, eBullets, powerUps, playerNumber, False)))
        redrawWINdow(WIN, players[playerNumber], players[(playerNumber+1)%2], enemies, eBullets, powerUps)


        #variable = gameDate(p1, enemies, eBullets, powerUps, seconds)
        #data_string = pickle.dumps(variable)
        #n.send(data_string)

    pygame.quit()


if __name__ == '__main__':
    play()