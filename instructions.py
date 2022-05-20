
import sys
from textwrap import wrap

import menu
from client.variables import INST, INSTRUCTION_FONT, END_QUIT, WHITE, WIDTH, HEIGHT, FPS, bg, BLACK
import pygame


def instruction(WIN):
    width = 740
    height =340
    f = open(INST, "r")
    lines = f.readlines()
    Texts =[]
    for line in lines:
        line = line.strip('\n')
        Text = INSTRUCTION_FONT.render(line, 1, WHITE)
        Texts.append(Text)

    Return = END_QUIT.render("Menu", 1, WHITE)

    clock = pygame.time.Clock()
    run = True

    buttonw = 370
    buttonh = 50
    buttonx = WIDTH / 2 - buttonw/2
    buttony = (HEIGHT / 1.2)
    padding = 20

    quitb = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    quitw = pygame.Rect(buttonx - 1, buttony - 1, buttonw + 2, buttonh + 2)

    while run:
        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()

        WIN.blit(bg, (0, 0))
        pygame.draw.rect(WIN, WHITE, ((WIDTH / 2 - width / 2) - 1, (HEIGHT / 12 ) - 1, width+2, height + 2))
        pygame.draw.rect(WIN, BLACK, (WIDTH/2-width/2, HEIGHT/12, width, height))

        y = height / 7
        for line in range (len(lines)):
            WIN.blit(Texts[line], (WIDTH/8.2, y + 5))
            y+=padding

        pygame.draw.rect(WIN, WHITE, quitw)
        pygame.draw.rect(WIN, BLACK, quitb)

        WIN.blit(Return, (buttonx + buttonw / 2 - 63, buttony + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitb.collidepoint((mx, my)):
                    f.close()
                    run = False
                    menu.menu()

        pygame.display.update()