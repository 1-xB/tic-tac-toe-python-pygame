import pygame
from sys import exit
import random


def is_draw():
    for i in gameplay:
        for j in i:
            if j == '0':
                return False
    return True

def music():
    return pygame.mixer.music.get_busy()


gameplay = [
    ['0', '0', '0'],
    ['0', '0', '0'],
    ['0', '0', '0']
]

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.008)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Tic Tac Toe')

clock = pygame.time.Clock()

word_big = pygame.image.load('imgs/tic.png')
word = pygame.transform.scale(word_big, (word_big.get_width() / 1.9, word_big.get_height() / 1.9))

font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 80)
font2 = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 12)

play_big = pygame.image.load('imgs/play.png')
play = pygame.transform.scale(play_big, (play_big.get_width() / 3, play_big.get_height() / 3))
play_rect = play.get_rect(center=(250, 350))

restart_big = pygame.image.load('imgs/restart.png')
restart = pygame.transform.scale(restart_big, (restart_big.get_width() / 4, restart_big.get_height() / 4))
restart_rect = restart.get_rect(center=(250, 450))

quit_big = pygame.image.load('imgs/quit.png')
quit = pygame.transform.scale(quit_big, (quit_big.get_width() / 3, quit_big.get_height() / 3))
quit_rect = quit.get_rect(center=(460, 460))

click = pygame.mixer.Sound('Music/click.mp3')
click.set_volume(0.05)

#kwadraty
# 1 poziomo
k1_1 = pygame.Rect(100, 102, 96, 94)
x1_1 = 100, 102
k1_2 = pygame.Rect(203, 102, 94, 94)
x1_2 = 203, 102
k1_3 = pygame.Rect(303, 102, 94, 94)
x1_3 = 303, 102
# 2 poziomo
k2_1 = pygame.Rect(100, 202, 96, 94)
x2_1 = 100, 202
k2_2 = pygame.Rect(203, 202, 94, 94)
x2_2 = 203, 202
k2_3 = pygame.Rect(303, 202, 94, 94)
x2_3 = 303, 202
# 3 poziomo
k3_1 = pygame.Rect(100, 302, 96, 94)
x3_1 = 100, 302
k3_2 = pygame.Rect(203, 302, 94, 94)
x3_2 = 203, 302
k3_3 = pygame.Rect(303, 302, 94, 94)
x3_3 = 303, 302

o_ = pygame.image.load('imgs/o.png')
o = pygame.transform.scale(o_, (95, 95))
x_ = pygame.image.load('imgs/x.png')
x = pygame.transform.scale(x_, (95, 95))

Author = font2.render('Game created by Piotr Zarzycki', True, 'black')

choice = [
    ['0', '0', '0'],
    ['0', '0', '0'],
    ['0', '0', '0']
]

start_menu = True
game = False

x_turn = True
o_turn = False

win = False

draw = False

while True:

    draw = is_draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if play_rect.collidepoint(event.pos) and start_menu:
                start_menu = False
                game = True
                click.play()
            if restart_rect.collidepoint(event.pos) and (win or draw):
                click.play()
                win = False
                draw = False
                gameplay = [
                    ['0', '0', '0'],
                    ['0', '0', '0'],
                    ['0', '0', '0']
                ]

                choice = [
                    ['0', '0', '0'],
                    ['0', '0', '0'],
                    ['0', '0', '0']
                ]
            if quit_rect.collidepoint(event.pos) and (win or draw):
                click.play()
                win = False
                game = False
                start_menu = True
                draw = False
                gameplay = [
                    ['0', '0', '0'],
                    ['0', '0', '0'],
                    ['0', '0', '0']
                ]

                choice = [
                    ['0', '0', '0'],
                    ['0', '0', '0'],
                    ['0', '0', '0']
                ]
            elif quit_rect.collidepoint(event.pos) and start_menu:
                click.play()
                pygame.quit()
                exit()
        elif not win and event.type == pygame.MOUSEBUTTONDOWN:

            if k1_1.collidepoint(event.pos) and game:
                if gameplay[0][0] == '0':
                    if x_turn:
                        znak = 'X'
                        x_turn = False
                        o_turn = True
                    else:
                        znak = 'O'
                        x_turn = True
                        o_turn = False
                    gameplay[0][0] = znak
                    if x_turn:
                        x1 = x.get_rect(topleft=x1_1)
                        choice[0][0] = x1
                    else:
                        o1 = o.get_rect(topleft=x1_1)
                        choice[0][0] = o1
                    click.play()

            if k1_2.collidepoint(event.pos) and game:
                if gameplay[0][1] == '0':
                    if x_turn:
                        znak = 'X'
                        x_turn = False
                        o_turn = True
                    else:
                        znak = 'O'
                        x_turn = True
                        o_turn = False
                    gameplay[0][1] = znak
                    if x_turn:
                        x2 = x.get_rect(topleft=x1_2)
                        choice[0][1] = x2
                    else:
                        o2 = o.get_rect(topleft=x1_2)
                        choice[0][1] = o2
                    click.play()

            if k1_3.collidepoint(event.pos) and game:
                if gameplay[0][2] == '0':
                    if x_turn:
                        znak = 'X'
                        x_turn = False
                        o_turn = True
                    else:
                        znak = 'O'
                        x_turn = True
                        o_turn = False
                    gameplay[0][2] = znak
                    if x_turn:
                        x3 = x.get_rect(topleft=x1_3)
                        choice[0][2] = x3
                    else:
                        o3 = o.get_rect(topleft=x1_3)
                        choice[0][2] = o3
                    click.play()

            if k2_1.collidepoint(event.pos) and game:
                if gameplay[1][0] == '0':
                    if x_turn:
                        znak = 'X'
                        x_turn = False
                        o_turn = True
                    else:
                        znak = 'O'
                        x_turn = True
                        o_turn = False
                    gameplay[1][0] = znak
                    if x_turn:
                        x4 = x.get_rect(topleft=x2_1)
                        choice[1][0] = x4
                    else:
                        o4 = o.get_rect(topleft=x2_1)
                        choice[1][0] = o4

                    click.play()

            if k2_2.collidepoint(event.pos) and game:
                if gameplay[1][1] == '0':
                    if x_turn:
                        znak = 'X'
                        x_turn = False
                        o_turn = True
                    else:
                        znak = 'O'
                        x_turn = True
                        o_turn = False
                    gameplay[1][1] = znak
                    if x_turn:
                        x5 = x.get_rect(topleft=x2_2)
                        choice[1][1] = x5
                    else:
                        o5 = o.get_rect(topleft=x2_2)
                        choice[1][1] = o5
                    click.play()

            if k2_3.collidepoint(event.pos) and game:
                if gameplay[1][2] == '0':
                    if x_turn:
                        znak = 'X'
                        x_turn = False
                        o_turn = True
                    else:
                        znak = 'O'
                        x_turn = True
                        o_turn = False
                    gameplay[1][2] = znak
                    if x_turn:
                        x6 = x.get_rect(topleft=x2_3)
                        choice[1][2] = x6
                    else:
                        o6 = o.get_rect(topleft=x2_3)
                        choice[1][2] = o6
                    click.play()

            if k3_1.collidepoint(event.pos) and game:
                if gameplay[2][0] == '0':
                    if x_turn:
                        znak = 'X'
                        x_turn = False
                        o_turn = True
                    else:
                        znak = 'O'
                        x_turn = True
                        o_turn = False
                    gameplay[2][0] = znak
                    if x_turn:
                        x7 = x.get_rect(topleft=x3_1)
                        choice[2][0] = x7
                    else:
                        o7 = o.get_rect(topleft=x3_1)
                        choice[2][0] = o7
                    click.play()
            if k3_2.collidepoint(event.pos) and game:
                if gameplay[2][1] == '0':
                    if x_turn:
                        znak = 'X'
                        x_turn = False
                        o_turn = True
                    else:
                        znak = 'O'
                        x_turn = True
                        o_turn = False
                    gameplay[2][1] = znak
                    if x_turn:
                        x8 = x.get_rect(topleft=x3_2)
                        choice[2][1] = x8
                    else:
                        o8 = o.get_rect(topleft=x3_2)
                        choice[2][1] = o8
                    click.play()
            if k3_3.collidepoint(event.pos) and game:
                if gameplay[2][2] == '0':
                    if x_turn:
                        znak = 'X'
                        x_turn = False
                        o_turn = True
                    else:
                        znak = 'O'
                        x_turn = True
                        o_turn = False
                    gameplay[2][2] = znak
                    if x_turn:
                        x9 = x.get_rect(topleft=x3_3)
                        choice[2][2] = x9
                    else:
                        o9 = o.get_rect(topleft=x3_3)
                        choice[2][2] = o9
                    click.play()

    if not music():
        pygame.mixer.music.load(f'Music/music{random.randint(1, 5)}.mp3')
        pygame.mixer.music.play()

    screen.fill('#808080')

    if game:
        if x_turn and not win:
            screen.fill('#28bfb0')
            kolei = font.render('Move for X', True, 'black')
            screen.blit(kolei, (50, 10))
            color = '#28bfb0'
        if o_turn and not win:
            screen.fill('#b87127')
            kolei = font.render('Move for O', True, 'black')
            screen.blit(kolei, (50, 10))
            color = '#b87127'

        if win:
            color = '#808080'
            screen.fill('#808080')
            screen.blit(restart, restart_rect)
            screen.blit(quit, quit_rect)

            if x_turn and not draw:
                kolei = font.render('O has won', True, 'black')
                screen.blit(kolei, (60, 10))
            else:
                kolei = font.render('X has won', True, 'black')
                screen.blit(kolei, (60, 10))
        if not win and draw:
            color = '#808080'
            screen.fill('#808080')
            screen.blit(restart, restart_rect)
            screen.blit(quit, quit_rect)
            kolei = font.render('Draw', True, 'black')
            screen.blit(kolei, (115, 10))

        pygame.draw.line(screen, 'black', (100, 200), (400, 200), 5)
        pygame.draw.line(screen, 'black', (100, 300), (400, 300), 5)

        # Linie pionowe
        pygame.draw.line(screen, 'black', (200, 100), (200, 400), 5)
        pygame.draw.line(screen, 'black', (300, 100), (300, 400), 5)

        pygame.draw.rect(screen, color, k1_1)
        pygame.draw.rect(screen, color, k1_2)
        pygame.draw.rect(screen, color, k1_3)
        pygame.draw.rect(screen, color, k2_1)
        pygame.draw.rect(screen, color, k2_2)
        pygame.draw.rect(screen, color, k2_3)
        pygame.draw.rect(screen, color, k3_1)
        pygame.draw.rect(screen, color, k3_2)
        pygame.draw.rect(screen, color, k3_3)
        row = 0
        col = 0
        for i in range(len(choice)):
            for j in range(len(choice[i])):
                if gameplay[row][col] == 'X':
                    screen.blit(x, choice[row][col].topleft)
                elif gameplay[row][col] == 'O':
                    screen.blit(o, choice[row][col].topleft)
                col += 1
            row += 1
            col = 0

        if gameplay[0][0] == 'X' and gameplay[0][1] == 'X' and gameplay[0][2] == 'X':
            pygame.draw.line(screen, 'red', (100, 152), (400, 152), 15)
            win = True
        elif gameplay[1][0] == 'X' and gameplay[1][1] == 'X' and gameplay[1][2] == 'X':
            pygame.draw.line(screen, 'red', (100, 252), (400, 252), 15)
            win = True
        elif gameplay[2][0] == 'X' and gameplay[2][1] == 'X' and gameplay[2][2] == 'X':
            pygame.draw.line(screen, 'red', (100, 352), (400, 352), 15)
            win = True
        elif gameplay[0][0] == 'X' and gameplay[1][0] == 'X' and gameplay[2][0] == 'X':
            pygame.draw.line(screen, 'red', (150, 102), (150, 402), 15)
            win = True
        elif gameplay[0][1] == 'X' and gameplay[1][1] == 'X' and gameplay[2][1] == 'X':
            pygame.draw.line(screen, 'red', (250, 102), (250, 402), 15)
            win = True
        elif gameplay[0][2] == 'X' and gameplay[1][2] == 'X' and gameplay[2][2] == 'X':
            pygame.draw.line(screen, 'red', (350, 102), (350, 402), 15)
            win = True
        elif gameplay[0][0] == 'X' and gameplay[1][1] == 'X' and gameplay[2][2] == 'X':
            pygame.draw.line(screen, 'red', (102, 102), (402, 402), 25)
            win = True
        elif gameplay[0][2] == 'X' and gameplay[1][1] == 'X' and gameplay[2][0] == 'X':
            pygame.draw.line(screen, 'red', (402, 102), (102, 402), 25)
            win = True

        elif gameplay[0][0] == 'O' and gameplay[0][1] == 'O' and gameplay[0][2] == 'O':
            pygame.draw.line(screen, 'red', (100, 152), (400, 152), 15)
            win = True
        elif gameplay[1][0] == 'O' and gameplay[1][1] == 'O' and gameplay[1][2] == 'O':
            pygame.draw.line(screen, 'red', (100, 252), (400, 252), 15)
            win = True
        elif gameplay[2][0] == 'O' and gameplay[2][1] == 'O' and gameplay[2][2] == 'O':
            pygame.draw.line(screen, 'red', (100, 352), (400, 352), 15)
            win = True
        elif gameplay[0][0] == 'O' and gameplay[1][0] == 'O' and gameplay[2][0] == 'O':
            pygame.draw.line(screen, 'red', (150, 102), (150, 402), 15)
            win = True
        elif gameplay[0][1] == 'O' and gameplay[1][1] == 'O' and gameplay[2][1] == 'O':
            pygame.draw.line(screen, 'red', (250, 102), (250, 402), 15)
            win = True
        elif gameplay[0][2] == 'O' and gameplay[1][2] == 'O' and gameplay[2][2] == 'O':
            pygame.draw.line(screen, 'red', (350, 102), (350, 402), 15)
            win = True
        elif gameplay[0][0] == 'O' and gameplay[1][1] == 'O' and gameplay[2][2] == 'O':
            pygame.draw.line(screen, 'red', (102, 102), (402, 402), 25)
            win = True
        elif gameplay[0][2] == 'O' and gameplay[1][1] == 'O' and gameplay[2][0] == 'O':
            pygame.draw.line(screen, 'red', (402, 102), (102, 402), 25)
            win = True



    if start_menu:
        screen.blit(play, play_rect)
        screen.blit(word, (10, 20))
        screen.blit(quit, quit_rect)
        screen.blit(Author, (0, 485))


    clock.tick(60)
    pygame.display.update()
