import sys
import pygame

from animation.menuAnimation import Ship, drawShip, ReadFile
from client import game
from bin import game2
from client.variables import WHITE, BLACK, WIDTH, HEIGHT, OPTION_FONT, TITTLE_FONT, FPS, bg
from instructions import instruction

click = False

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship")

def drawText(WIN, playx, playy, multix, multiy, instx, insty, quitx, quity, widith):

    TitleText = TITTLE_FONT.render("SPACESHIP", 1, (255,255,255))
    WIN.blit(TitleText, (WIDTH/15, HEIGHT/15))

    PlayText = OPTION_FONT.render("Play", 1, (255,255,255))
    WIN.blit(PlayText, (playx + widith/2-63, playy +5))

    MultiText = OPTION_FONT.render("Multiplayer", 1, (255, 255, 255))
    WIN.blit(MultiText, (multix +10, multiy + 5))

    InstText = OPTION_FONT.render("Instruction", 1, (255, 255, 255))
    WIN.blit(InstText, (instx + 17, insty + 5))

    QuitText = OPTION_FONT.render("Quit", 1, (255, 255, 255))
    WIN.blit(QuitText, (quitx + widith / 2 - 63, quity + 5))


    pygame.display.update()

def menu():

    run = True
    clock = pygame.time.Clock()
    buttonw= 370
    buttonh= 50
    buttonx = WIDTH / 2 - buttonw/2
    buttony = (HEIGHT /2.5)
    padding = 10 + buttonh

    playb = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    playw = pygame.Rect(buttonx-1, buttony-1, buttonw+2, buttonh+2)

    buttony +=padding
    multib = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    multiw = pygame.Rect(buttonx-1, buttony-1, buttonw+2, buttonh+2)

    buttony += padding
    instb = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    instw = pygame.Rect(buttonx-1, buttony-1, buttonw+2, buttonh+2)

    buttony += padding
    quitb = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    quitw = pygame.Rect(buttonx-1, buttony-1, buttonw+2, buttonh+2)

    animate = Ship(50,50,40,40,(0,255,0))
    reader = ReadFile(animate)


    while run:

        WIN.blit(bg, (0, 0))
        clock.tick(FPS)

        mx, my = pygame.mouse.get_pos()

        drawShip(WIN, animate, reader)

        pygame.draw.rect(WIN, WHITE, playw)
        pygame.draw.rect(WIN, BLACK, playb)
        pygame.draw.rect(WIN, WHITE, multiw)
        pygame.draw.rect(WIN, BLACK, multib)
        pygame.draw.rect(WIN, WHITE, instw)
        pygame.draw.rect(WIN, BLACK, instb)
        pygame.draw.rect(WIN, WHITE, quitw)
        pygame.draw.rect(WIN, BLACK, quitb)

        drawText(WIN, buttonx, buttony-(padding*3), buttonx, buttony-(padding*2), buttonx, buttony-padding, buttonx, buttony, buttonw)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if playb.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                game.play()
        if multib.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                game2.play()
        if instb.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                instruction(WIN)
        if quitb.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        pygame.display.update()