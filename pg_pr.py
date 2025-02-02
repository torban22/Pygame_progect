'''import pygame
import os
import time
import sys
from PIL import Image
from random import randint

from PIL.ImageChops import offset
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
        id = load_image(os.path.join('images', 'enemy',  'grass.png'))
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top,
                    self.cell_size, self.cell_size), 1)
                if self.board[y][x] == 0:
                    screen.blit(id[0], (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size, self.cell_size))



if __name__ == '__main__':
    global size, screen
    pygame.init()

    start_screen()
    second_screen()

    from pg_enemy import *

    #vrag = Vrag(n, enemies)
    n0 = 0
    n1 = 1
    n2 = 2
    n3 = 3
    vrag1 = Vrag(n0)
    vrag2 = Vrag(n1)
    vrag3 = Vrag(n2)
    vrag4 = Vrag(n3)
    #vrag5 = Vrag()
    spis_zomb = [vrag1, vrag2, vrag3, vrag4]
    step = 10
    board = Board(25, 13)
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
                    print('uservent')
                    if player.attack and jisn_igr >= 0:

                        #elem.get_hurt()
                        print(elem.indik)
                        print(spis_zomb)
                        #if elem.num >= len(spis_zomb):
                            #elem.num = len(spis_zomb) - 1
                            #print(elem.num)
                        spis_zomb[elem.num - 1].health -= uron_igr
                        print(spis_zomb[elem.num - 1].health)
                        #print(elem.num)

                    player.get_hurt()
                    if player.health <= 0:
                        lose_screen()
                        see_points()
                        running = False
                    if spis_zomb[elem.num - 1].health <= 0:
                        #win_screen()
                        #see_points()
                        #running = False
                        spis_zomb.remove(spis_zomb[elem.num - 1])
                        #elem.num -= 1
                        print(elem.num)
                        #elem.jisn = False
                        #count += 1
                    ch += 1
                if len(spis_zomb) == 0:
                    win_screen()
                    see_points()
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN and player.attack is False:
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

        screen.fill((50, 50, 50))
        #all_sprites.update()
        board.render(screen)
        player.draw()
        for elem in spis_zomb:
            ind1 = spis_zomb.index(elem)
            print(f'индекс нарисованного {ind1}')
            elem.draw(ind1)
        screen.blit(player.imp, (player.x, player.y))
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()'''

import pygame
import os
import time
import sys
from PIL import Image
from random import randint

from PIL.ImageChops import offset
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
        id = load_image(os.path.join('images', 'enemy',  'grass.png'))
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top,
                    self.cell_size, self.cell_size), 1)
                if self.board[y][x] == 0:
                    screen.blit(id[0], (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size, self.cell_size))



if __name__ == '__main__':
    global size, screen
    pygame.init()

    start_screen()
    second_screen()

    from pg_enemy import *

    #vrag = Vrag(n, enemies)

    vrag1 = Vrag()
    vrag2 = Vrag()
    vrag3 = Vrag()
    vrag4 = Vrag()
    #vrag5 = Vrag()
    spis_zomb = [vrag1, vrag2, vrag3, vrag4]
    step = 10
    board = Board(25, 13)
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
                    print('uservent')
                    if player.attack and jisn_igr >= 0:

                        #elem.get_hurt()

                        spis_zomb[elem.num - 1].health -= uron_igr
                        print(spis_zomb[elem.num - 1].health)
                        print(elem.num - 1)
                        print(spis_zomb)
                    player.get_hurt()
                    if player.health <= 0:
                        lose_screen()
                        see_points()
                        running = False
                    if spis_zomb[elem.num - 1].health <= 0:
                        '''win_screen()
                        see_points()
                        running = False'''
                        spis_zomb.remove(spis_zomb[elem.num - 1])
                        elem.num = len(spis_zomb)
                        print(elem.num)
                        #elem.jisn = False
                        #count += 1
                    ch += 1
                if len(spis_zomb) == 0:
                    win_screen()
                    see_points()
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN and player.attack is False:
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

        screen.fill((50, 50, 50))
        #all_sprites.update()
        board.render(screen)
        player.draw()
        for elem in spis_zomb:
            ind1 = spis_zomb.index(elem)
            print(f'индекс нарисованного {ind1}')
            elem.draw(ind1)
        screen.blit(player.imp, (player.x, player.y))
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()