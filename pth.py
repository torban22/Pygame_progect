import pygame
import os
import time
import sys
from PIL import Image
from random import randint

from PIL.ImageChops import offset


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

jisn_igr = 300
jisn_zomb = 400
running = True




class Vrag(pygame.sprite.Sprite):
    def __init__(self, n, group):
        super().__init__(all_sprites)
        global mask_enem
        self.koords = []
        self.step = 1
        self.helth = jisn_zomb
        cor = self.poisk()
        self.koords = cor



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
                     load_image(os.path.join('images', 'enemy',  'Dead5.png'))]

        self.image = self.run1[0]
        self.move = True
        self.jisn = True
        self.rect = self.image[0].get_rect()
        self.mask = pygame.mask.from_surface(self.image[0])
        self.add(group)
        mask_enem = pygame.mask.from_surface(self.image[0])

        self.frame = 0  # текущий кадр
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 10  # как быстро кадры меняются


    def poisk(self):
        b = (randint(100, 700), randint(50, 100))
        return b


    def draw(self):
        global ofset, jisn_igr, jisn_zomb, running
        kord = player.get_pos()
        now = pygame.time.get_ticks()
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
                #ind1 = self.koords.index(elem)
                #self.koords.insert(ind1, elem1)
                self.koords = elem1
            else:
                elem1 = (self.koords[0] - self.step, self.koords[1] + self.step)
                #ind1 = self.koords.index(elem)
                #self.koords.insert(ind1, elem1)
                self.koords = elem1
        if self.koords[1] > kord[1]:
            if self.koords[0] < kord[0]:
                elem1 = (self.koords[0] + self.step, self.koords[1] - self.step)
                #ind1 = self.koords.index(elem)
                #self.koords.insert(ind1, elem1)
                self.koords = elem1
            else:
                elem1 = (self.koords[0] - self.step, self.koords[1] - self.step)
                #ind1 = self.koords.index(elem)
                #self.koords.insert(ind1, elem1)
                self.koords = elem1
        if self.koords[1] == kord[1]:
            if self.koords[0] < kord[0]:
                elem1 = (self.koords[0] + self.step, self.koords[1])
                #ind1 = self.koords.index(elem)
                #self.koords.insert(ind1, elem1)
                self.koords = elem1
            else:
                elem1 = (self.koords[0] - self.step, self.koords[1])
                #ind1 = self.koords.index(elem)
                #self.koords.insert(ind1, elem1)
                self.koords = elem1

            # при столкновении появляется событи USERVENT
        if mask_play.overlap_area(mask_enem, ofset) > 0:
            print('KKGJGJGJFJG')
            self.move = False
            pygame.time.set_timer(pygame.USEREVENT, 100, True)
            if jisn_zomb <= 0:
                self.jisn = False
            print(jisn_igr)

        elif not mask_play.overlap_area(mask_enem, ofset) > 0:
            self.move = True

        if not self.move and self.jisn:
            self.image = self.atack[0]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(self.atack) - 1:
                    self.frame = 0
                self.image = self.atack[self.frame]

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
                print(self.frame)
                if self.frame == 4:
                    running = False
                    pygame.time.wait(1000)
        print(self.move)






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
                if self.board[x][y] == 0:
                    screen.blit(id[0], (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size, self.cell_size))



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        global mask_play

        self.x = 375
        self.y = 375
        self.right = False
        self.left = False
        self.up = False
        self.down = True
        self.step = 0
        self.rotate = 0
        self.move = False

        self.health = 300
        self.attack = False


        #idle
        self.idle_down = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'Idle', 'idleDown.gif'))
        self.idle_up = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'Idle', 'idleUp.gif'))
        self.idle_right = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'Idle', 'idleRight.gif'))
        self.idle_left = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'Idle', 'idleLeft.gif'))
        #run
        self.run_down = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'run', 'runDown.gif'))
        self.run_up = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'run', 'runUp.gif'))
        self.run_right = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'run', 'runRight.gif'))
        self.run_left = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'run', 'runLeft.gif'))
        #attack
        self.attack_down = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'attack1', 'attack1Down.gif'))
        self.attack_up= split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'attack1', 'attack1Up.gif'))
        self.attack_right = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'attack1', 'attack1Right.gif'))
        self.attack_left = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'attack1', 'attack1Left.gif'))

        self.image = self.idle_down[0]
        self.rect = self.image.get_rect()
        mask_play = pygame.mask.from_surface(self.image)


    def draw(self):
        global last_update, animation_cooldown
        imp = None
        cur_time = pygame.time.get_ticks()
        if self.step >= 3:
            self.step = 0
        if cur_time - last_update >= animation_cooldown:
            self.step += 1
            last_update = cur_time
        if self.down and self.attack:
            imp = self.attack_down[self.step]
            self.attack = False
        elif self.up and self.attack:
            imp = self.attack_up[self.step]
            self.attack = False
        elif self.right and self.attack:
            imp = self.attack_right[self.step]
            self.attack = False
        elif self.left and self.attack:
            imp = self.attack_left[self.step]
            self.attack = False
        elif self.down and self.move is False:
            imp = self.idle_down[self.step]
        elif self.right and self.move is False:
            imp = self.idle_right[self.step]
        elif self.left and self.move is False:
            imp = self.idle_left[self.step]
        elif self.up and self.move is False:
            imp = self.idle_up[self.step]
        elif self.down and self.move:
            imp = self.run_down[self.step]
        elif self.right and self.move:
            imp = self.run_right[self.step]
        elif self.left and self.move:
            imp = self.run_left[self.step]
        elif self.up and self.move:
            imp = self.run_up[self.step]
        if imp:
            self.image = imp
            screen.blit(imp, (self.x, self.y))


    def load_image(self, name1, name2, colorkey=None):
        fullname = os.path.join('images', 'player', 'knight', 'GIFs', name1, name2)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def get_pos(self):
        return [self.x, self.y]

    def get_field_pos(self):
        return [self.x // 60, self.y // 60]

def split_animated_gif(gif_file_path):
    ret = []
    gif = Image.open(gif_file_path)
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode)
        ret.append(pygame_image)
    return ret


def terminate():
    pygame.quit()
    sys.exit()
# Заставка
def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры:",
                  "Игроку нужно убить зомби"]
    WIDTH = 800
    HEIGHT = 800
    screen = pygame.display.set_mode([800, 800])
    fon = pygame.transform.scale(load_im('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(50)





if __name__ == '__main__':
    pygame.init()
    n = 5
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    size = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Игра')
    clock = pygame.time.Clock()
    vrag1 = Vrag(n, enemies)
    vrag2 = Vrag(n, enemies)
    vrag3 = Vrag(n, enemies)
    vrag4 = Vrag(n, enemies)
    vrag5 = Vrag(n, enemies)
    step = 10

    board = Board(13, 13)
    screen.fill((50, 50, 50))
    board.render(screen)
    start_screen()
    player = Player()
    val = 10
    animation_cooldown = 150
    uron_zomb = 10
    uron_igr = 50
    sp = [vrag1, vrag2, vrag3, vrag4, vrag5]



    last_update = pygame.time.get_ticks()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #running = False
                terminate()
            # при вызове события урон получают оба позже изменю
            elif event.type == pygame.USEREVENT:
                print('kurva')
                jisn_igr -= uron_zomb
                jisn_zomb -= uron_igr
                print(jisn_igr)
                print(jisn_zomb)

                if jisn_igr <= 0:
                    running = False
                    print('ПОБЕДА ЗОМБИ')
                if jisn_zomb <= 0:
                    print('ПОБЕДА ИГРОКА!!!!!!!!!!!!!!!!!')
                    running = False



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
        for elem in sp:
            elem.draw()
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()