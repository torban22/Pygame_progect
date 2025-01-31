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

    vrag = Vrag(n, enemies)
    step = 10
    board = Board(25, 13)
    running = True
    board.render(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #running = False
                terminate()
            # при вызове события урон получают оба позже изменю
            elif event.type == pygame.USEREVENT:
                if player.attack and jisn_igr >= 0:
                    vrag.get_hurt()
                player.get_hurt()

                if player.health <= 0:
                    lose_screen()
                    see_points()
                    running = False
                if vrag.health <= 0:
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
        screen.blit(player.imp, (player.x, player.y))
        vrag.draw()
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()