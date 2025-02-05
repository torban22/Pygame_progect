# Сделал волны в зависимости от уровня если 1 то одна волна если 2 то две волны и тд, волны идут по 5 зомби
#  Рекорд не выводится на 2 и 3 уровнях
# класс босса прописал на скорую руку, вроде работае +- (только поправить урон) правда выводится он только в первой волне, при встрече обговорим как игде его выводить





import pygame
import os
import time
import sys
from PIL import Image
from random import randint

from start_screens import *


def load_image(gif_file_path):
    ret = []
    gif = Image.open(gif_file_path)
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode)
        ret.append(pygame_image)
    return ret

def load_im(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 60

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        id = load_image(os.path.join('images', 'fons',  'grass.png'))
        id1 = load_image(os.path.join('images', 'fons',  'ships.png'))
        id2 = load_image(os.path.join('images', 'fons',  'help.png'))
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top,
                    self.cell_size, self.cell_size), 1)
                if self.board[y][x] == 0:
                    screen.blit(id[0], (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size, self.cell_size))
                if self.board[y][x] == 1:
                    screen.blit(id1[0], (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size, self.cell_size))
                if self.board[y][x] == 2:
                    screen.blit(id2[0], (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size, self.cell_size))



if __name__ == '__main__':
    global size, screen
    pygame.init()

    start_screen()
    second_screen()

    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join('sounds', 'battle.mp3'))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)

    kolvo = 1

    from pg_enemy import *
    from boss import *

    vrag1 = Vrag(n0)
    vrag2 = Vrag(n1)
    vrag3 = Vrag(n2)
    vrag4 = Vrag(n3)
    vrag5 = Vrag(n4)

    vrag6 = Vrag(n5)
    vrag7 = Vrag(n6)
    vrag8 = Vrag(n7)
    vrag9 = Vrag(n8)
    vrag0 = Vrag(n9)

    vrag11 = Vrag(n11)
    vrag12 = Vrag(n12)
    vrag13 = Vrag(n13)
    vrag14 = Vrag(n14)
    vrag15 = Vrag(n15)

    spis_zomb = [vrag1, vrag2, vrag3, vrag4, vrag5]
    maso = [[vrag1, vrag2, vrag3, vrag4, vrag5], [vrag6, vrag7, vrag8, vrag9, vrag0], [vrag11, vrag12, vrag13, vrag14, vrag15]]

    board = Board(24, 13)
    from start_screens import LEVEL
    if LEVEL == 1:
        board.board[0][2] = 1
        board.board[2][5] = 1
        board.board[3][7] = 1
        board.board[9][1] = 1
        board.board[9][9] = 1
        board.board[11][23] = 1
        board.board[12][8] = 1
        board.board[10][19] = 1
        board.board[4][17] = 1
        board.board[5][19] = 1
        board.board[2][12] = 1
        board.board[6][10] = 2
        kolvo = 1
    if LEVEL == 2:
        for i in range(21):
            board.board[0][i] = 1
        for i in range(10):
            board.board[2][i] = 1
        for i in range(7, 22):
            board.board[5][i] = 1
        for i in range(18, 22):
            board.board[10][i] = 1
        for i in range(22):
            board.board[12][i] = 1
        for i in range(17):
            board.board[8][i] = 1
        board.board[11][23] = 1
        board.board[12][8] = 1
        board.board[10][19] = 1
        board.board[10][19] = 1

    if LEVEL == 3:
        for i in range(22):
            board.board[0][i] = 1
            board.board[1][i] = 1
        for i in range(22):
            board.board[12][i] = 1
            board.board[11][i] = 1
        for i in range(13):
            board.board[i][0] = 1
        for i in range(13):
            board.board[i][22] = 1
        board.board[5][15] = 1
        board.board[7][8] = 1
        board.board[9][5] = 1
        board.board[8][17] = 1
        board.board[4][6] = 1
    running = True
    board.render(screen)
    count = 0
    while running:
        for event in pygame.event.get():
            ch = 0
            for elem in spis_zomb:
                if ch >= 1:
                    break
                if event.type == pygame.QUIT:
                    #running = False
                    terminate()
                # пи вызове события урон получают оба позже изменю
                elif event.type == pygame.USEREVENT:
                    if jisn_igr >= 0:
                        player.get_hurt()
                    ch += 1
            if volna <= 2:
                enem = pygame.sprite.spritecollideany(player.sword, maso[volna])
            if event.type == pygame.MOUSEBUTTONDOWN and volna <= 2 and enem and player.attack:
                enem.get_hurt()
            elif event.type == pygame.MOUSEBUTTONDOWN and player.attack is False:
                sound3 = pygame.mixer.Sound(os.path.join('sounds', 'udar_v_vozduh.mp3'))
                sound3.play()
                sound3.set_volume(0.5)
                player.attack = True
                player.step = 0
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_UP]:
            player.y -= val
            player.right = False
            player.left = False
            player.up = True
            player.down = False
        if userInput[pygame.K_LEFT]:
            player.x -= val
            player.right = False
            player.left = True
            player.up = False
            player.down = False
        if userInput[pygame.K_RIGHT]:
            player.x += val
            player.right = True
            player.left = False
            player.up = False
            player.down = False
        if userInput[pygame.K_DOWN]:
            player.y += val
            player.right = False
            player.left = False
            player.up = False
            player.down = True
        if userInput[pygame.K_UP] or userInput[pygame.K_DOWN] or userInput[pygame.K_RIGHT] or userInput[pygame.K_LEFT]:
            player.move = True
        else:
            player.move = False
        if board.board[player.get_field_pos()[1]][player.get_field_pos()[0]] == 1:
            player.get_hurt()
        elif board.board[player.get_field_pos()[1]][player.get_field_pos()[0]] == 2:
            board.board[player.get_field_pos()[1]][player.get_field_pos()[0]] = 0
            player.health_up()
        if player.life is False:
            lose_screen()
            see_points()
            running = False
        screen.fill((50, 50, 50))
        board.render(screen)
        if volna == LEVEL:
            win_screen()
            see_points()
        if volna == 2:
            boss.draw()
        kills = 0
        if volna < LEVEL:
            lst = maso[volna]
            for elem in lst:
                elem.draw()
                a = all([i.health <= 0 for i in lst])
                if a:
                    kills += 1
                    a = False
                    if kills == len(spis_zomb):
                        poln += 1
                        if poln == 1:
                            volna = 1
                        elif poln == 2:
                            volna = 2
                            boss = Boss()
                        elif poln == 3:
                            volna = 3
        if player.health <= 150 and cur_time - last >= 8000:
            last = pygame.time.get_ticks()
            coords = [randint(0, 23), randint(0, 12)]
            while board.board[coords[1]][coords[0]] != 0:
                coords = [randint(0, 23), randint(0, 12)]
            board.board[coords[1]][coords[0]] = 2
            sound4 = pygame.mixer.Sound(os.path.join('sounds', 'get_heil_on_board.mp3'))
            sound4.play()
            sound4.set_volume(2)
        cur_time = pygame.time.get_ticks()
        player.draw()
        screen.blit(player.imp, (player.x, player.y))
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()