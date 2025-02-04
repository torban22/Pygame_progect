import pygame
import os
import time
import sys
from PIL import Image
from random import randint


from pg_player import player, mask_play
from pg_screen import *
from start_screens import *
NUM = 0

class Vrag(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__(all_sprites)
        global mask_enem
        self.koords = []
        self.indik  = n
        self.step = 2
        self.health = 400
        cor = self.poisk()
        self.num = 0
        self.koords = cor
        self.end = False



        # idle
        self.idle1 = [load_image(os.path.join('images', 'enemy',  'Idle1.png')), load_image(os.path.join('images', 'enemy',  'Idle2.png')),
                      load_image(os.path.join('images', 'enemy',  'Idle3.png')), load_image(os.path.join('images', 'enemy',  'Idle4.png'))]

        # run
        self.run1 = [
                     load_image(os.path.join('images', 'enemy',  'Run4.png')),
                     load_image(os.path.join('images', 'enemy',  'Run5.png')),
                     load_image(os.path.join('images', 'enemy',  'Run6.png')), load_image(os.path.join('images', 'enemy',  'Run7.png')),
                     load_image(os.path.join('images', 'enemy',  'Run8.png')),
                     load_image(os.path.join('images', 'enemy',  'Run9.png'))]
        # atack
        self.atack = [load_image(os.path.join('images', 'enemy',  'Attack1.png')), load_image(os.path.join('images', 'enemy',  'Attack2.png')),
                      load_image(os.path.join('images', 'enemy',  'Attack3.png')), load_image(os.path.join('images', 'enemy',  'Attack4.png')),
                      load_image(os.path.join('images', 'enemy',  'Attack5.png')), load_image(os.path.join('images', 'enemy',  'Attack6.png'))]
        #walk
        self.walk = [load_image(os.path.join('images', 'enemy',  'Walk1.png')), load_image(os.path.join('images', 'enemy',  'Walk2.png')),
                     load_image(os.path.join('images', 'enemy',  'Walk3.png')), load_image(os.path.join('images', 'enemy',  'Walk4.png')),
                     load_image(os.path.join('images', 'enemy',  'Walk5.png')), load_image(os.path.join('images', 'enemy',  'Walk6.png'))]
        #dead
        self.dead = [load_image(os.path.join('images', 'enemy',  'Dead1.png')), load_image(os.path.join('images', 'enemy',  'Dead2.png')),
                     load_image(os.path.join('images', 'enemy',  'Dead3.png')), load_image(os.path.join('images', 'enemy',  'Dead4.png')),
                     load_image(os.path.join('images', 'enemy',  'Dead5.png')), load_image(os.path.join('images', 'enemy',  'Dead6.png')),
                     load_image(os.path.join('images', 'enemy',  'Dead7.png')), load_image(os.path.join('images', 'enemy',  'Dead8.png'))]

        self.image = self.run1[0]
        self.move = True
        self.jisn = True
        self.rect = self.image[0].get_rect()
        self.mask = pygame.mask.from_surface(self.image[0])
        #self.add(group)
        mask_enem = pygame.mask.from_surface(self.image[0])

        self.frame = 0  # текущий кадр
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 10  # как быстро кадры меняются


    def poisk(self):
        b = (randint(100, 700), randint(50, 100))
        return b


    def draw(self):
        global ofset, jisn_igr, jisn_zomb, running, numb
        if self.end:
            return
        kord = player.get_pos()
        now = pygame.time.get_ticks()
        if not self.jisn:
            self.image = self.dead[0]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(self.dead):
                    self.frame = 0
                if self.frame > len(self.dead):
                    self.frame = len(self.dead)
                self.image = self.dead[self.frame]
                #print(self.frame)
                if self.frame == 7:
                    print(0)
                    running = False
                    self.end = True
                    pygame.time.wait(10)
        if self.move and self.jisn:
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(self.run1) - 1:
                    self.frame = 0
                self.image = self.run1[self.frame]

        screen.blit(self.image[0], (self.koords[0], self.koords[1]))
        ofset = (self.koords[0] - kord[0], self.koords[1] - kord[1])
        if self.koords[1] < kord[1]:
            if self.koords[0] < kord[0]:
                elem1 = (self.koords[0] + self.step, self.koords[1] + self.step)
                # ind1 = self.koords.index(elem)
                # self.koords.insert(ind1, elem1)
                self.koords = elem1
            else:
                elem1 = (self.koords[0] - self.step, self.koords[1] + self.step)
                # ind1 = self.koords.index(elem)
                # self.koords.insert(ind1, elem1)
                self.koords = elem1
        if self.koords[1] > kord[1]:
            if self.koords[0] < kord[0]:
                elem1 = (self.koords[0] + self.step, self.koords[1] - self.step)
                # ind1 = self.koords.index(elem)
                # self.koords.insert(ind1, elem1)
                self.koords = elem1
            else:
                elem1 = (self.koords[0] - self.step, self.koords[1] - self.step)
                # ind1 = self.koords.index(elem)
                # self.koords.insert(ind1, elem1)
                self.koords = elem1
        if self.koords[1] == kord[1]:
            if self.koords[0] < kord[0]:
                elem1 = (self.koords[0] + self.step, self.koords[1])
                # ind1 = self.koords.index(elem)
                # self.koords.insert(ind1, elem1)
                self.koords = elem1
            else:
                elem1 = (self.koords[0] - self.step, self.koords[1])
                # ind1 = self.koords.index(elem)
                # self.koords.insert(ind1, elem1)
                self.koords = elem1

            # при столкновении появляется событи USERVENT
        if mask_play.overlap_area(mask_enem, ofset) > 0:
            self.move = False
            NUM = self.indik
            print(f'номер с кем столкнулся {NUM}')
            if player.attack and player.health >= 0:
                self.get_hurt()
            pygame.time.set_timer(pygame.USEREVENT, 100, True)
            player.boss = False
            if self.health <= 0:
                self.jisn = False
            #print(jisn_igr)

        elif not mask_play.overlap_area(mask_enem, ofset) > 0:
            self.move = True

        if player.sword.mask.overlap_area(mask_enem, ofset) > 0:
            self.move = False
            NUM = self.indik
            print(f'номер с кем столкнулся {NUM}!!!!!!!')
            if player.attack and player.health >= 0:
                self.get_hurt()

        if not self.move and self.jisn:
            self.image = self.atack[0]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(self.atack) - 1:
                    self.frame = 0
                self.image = self.atack[self.frame]
        #print(self.move)

    def draw_health(self):
        pygame.draw.rect(screen, 'red', (1400 - self.health, 10, 1400, 30))
        pygame.display.flip()

    def get_hurt(self):
        if self.health > 0:
            self.health -= uron_igr
        d = dt.datetime.now() - player.last_time
        if d.seconds > 0:
            player.points()




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
        id = load_image(os.path.join('images', 'enemy', 'grass.png'))
        # id1 = load_image(os.path.join('images', 'enemy',  'ships.png'))
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top,
                    self.cell_size, self.cell_size), 1)
                if self.board[y][x] == 0 or self.board[y][x] == 1:
                    screen.blit(id[0], (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size, self.cell_size))
                '''if self.board[y][x] == 1:
                    screen.blit(id1[0], (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size, self.cell_size))'''


if __name__ == '__main__':
    global size, screen
    pygame.init()

    start_screen()
    second_screen()
    kolvo = 1

    from pg_enemy import *
    from boss import *

    boss = Boss()
    n0 = 0
    n1 = 1
    n2 = 2
    n3 = 3
    n4 = 4
    n5 = 5
    n6 = 6
    n7 = 7
    n8 = 8
    n9 = 9
    n11 = 10
    n12 = 11
    n13 = 12
    n14 = 13
    n15 = 14
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
    maso = [[vrag1, vrag2, vrag3, vrag4, vrag5], [vrag6, vrag7, vrag8, vrag9, vrag0], [boss]]
    step = 10

    volna = 0
    poln = 0

    board = Board(25, 13)
    from start_screens import LEVEL

    if LEVEL == 1:
        board.board[0][2] = 1
        board.board[2][5] = 1
        board.board[3][7] = 1
        board.board[9][1] = 1
        kolvo = 1
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
                    # running = False
                    terminate()
                # пи вызове события урон получают оба позже изменю
                elif event.type == pygame.USEREVENT:
                    print('uservent')
                    if player.attack and jisn_igr >= 0:
                        '''#elem.get_hurt()
                        print(elem.indik)
                        print(elem.num)
                        #if elem.num >= len(spis_zomb):
                            #elem.num = len(spis_zomb) - 1
                            #print(elem.num)
                        spis_zomb[NUM].health -= uron_igr
                        print(NUM)
                        #print(elem.num)'''

                    player.get_hurt()
                    if player.health <= 0:
                        lose_screen()
                        see_points()
                        running = False
                    # a = all([i.health <= 0 for i in spis_zomb])
                    # if a:
                    #   win_screen()
                    #  see_points()
                    # running = False
                    # spis_zomb.remove(spis_zomb[elem.num - 1])
                    # elem.num -= 1
                    # print(elem.num)
                    # elem.jisn = False
                    # count += 1
                    ch += 1
                '''if len(spis_zomb) == 0:
                    win_screen()
                    see_points()
                    running = False'''

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
        if board.board[player.get_field_pos()[1]][player.get_field_pos()[0]] == 1:
            print('АААА кактус!')
            player.get_hurt()
        screen.fill((50, 50, 50))
        # all_sprites.update()
        board.render(screen)
        player.draw()
        screen.blit(player.imp, (player.x, player.y))
        '''if LEVEL == 1:
            for elem in spis_zomb:
                ind1 = spis_zomb.index(elem)
                elem.draw(ind1)'''
        '''for i in range(LEVEL):
            maso.append(spis_zomb)'''

        if volna == LEVEL:
            win_screen()
            see_points()

        enem = pygame.sprite.spritecollideany(player.sword, maso[volna])
        print(enem)
        if enem and player.attack:
            print(111111111)
            enem.get_hurt()
        kills = 0
        print(f'килы {kills}')
        if volna < LEVEL:
            print(f'волна {volna}')
            lst = maso[volna]
            for elem in lst:
                # ind1 = spis_zomb.index(elem)
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
                        elif poln == 3:
                            volna = 3

        pygame.display.flip()
        clock.tick(10)
    pygame.quit()