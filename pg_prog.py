import pygame
import os
import sys
from PIL import Image
from random import randint


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


'''def load_ime(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image'''




class Vrag(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__(all_sprites)
        self.koords = []
        self.step = 1
        for i in range(n):
            cor = self.poisk()
            self.koords.append(cor)



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
        self.rect = self.image[0].get_rect()
        print(self.rect)
        # self.rect.center = center
        self.frame = 0  # текущий кадр
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 10  # как быстро кадры меняются



    def poisk(self):
        b = (randint(100, 700), randint(50, 100))
        return b


    def draw(self):
        kord = player.get_pos()
        now = pygame.time.get_ticks()
        if self.move:
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(self.run1) - 1:
                    self.frame = 0
                self.image = self.run1[self.frame]

        for elem in self.koords:
            screen.blit(self.image[0], (elem[0], elem[1]))
            if elem[1] < kord[1]:
                if elem[0] < kord[0]:
                    elem1 = (elem[0] + self.step, elem[1] + self.step)
                    ind1 = self.koords.index(elem)
                    self.koords.insert(ind1, elem1)
                    self.koords.remove(elem)
                else:
                    elem1 = (elem[0] - self.step, elem[1] + self.step)
                    ind1 = self.koords.index(elem)
                    self.koords.insert(ind1, elem1)
                    self.koords.remove(elem)
            if elem[1] > kord[1]:
                if elem[0] < kord[0]:
                    elem1 = (elem[0] + self.step, elem[1] - self.step)
                    ind1 = self.koords.index(elem)
                    self.koords.insert(ind1, elem1)
                    self.koords.remove(elem)
                else:
                    elem1 = (elem[0] - self.step, elem[1] - self.step)
                    ind1 = self.koords.index(elem)
                    self.koords.insert(ind1, elem1)
                    self.koords.remove(elem)

            elif elem[1] == kord[1] and elem[0] == kord[0]:
                self.move = False
            elif elem[1] != kord[1] and elem[0] != kord[0]:
                self.move = True
        if not self.move:
            self.image = self.atack[0]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(self.atack) - 1:
                    self.frame = 0
                self.image = self.atack[self.frame]




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
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (400, 400, 60, 60), 1)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.x = 375
        self.y = 375
        self.attack_time = 4
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

        self.draw()


    def draw(self):
        global last_update, animation_cooldown
        imp = None
        cur_time = pygame.time.get_ticks()
        if self.step >= 3:
            self.step = 0
            if self.attack:
                self.attack = False
        if cur_time - last_update >= animation_cooldown:
            self.step += 1
            last_update = cur_time

        if self.down and self.attack:
            imp = self.attack_down[self.step]
        elif self.up and self.attack:
            imp = self.attack_up[self.step]
        elif self.right and self.attack:
            imp = self.attack_right[self.step]
        elif self.left and self.attack:
            imp = self.attack_left[self.step]

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
            self.rect = imp.get_rect()
            self.mask = pygame.mask.from_surface(imp)
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

def start_screen():
    intro_text = ["РЫЦАРСКИЙ БОЙ", "",
                  "Правила игры",
                  "",
                  "Вша задача - успешно пройти все уровни, не потеряв все здорововье,",
                  "которое вы имеете. Но вам будут мешать кровожадные зомби,",
                  "которых необходимо уничтожить.",
                  "Чем быстрее вы это сделаете, тем больше очков получите"]

    fon = pygame.transform.scale(load_image1('mountains.png'), (1400, 800))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect(center=(1400 / 2, 800))
        text_coord += 10
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    button_surface = pygame.Surface((200, 100))
    button_rect = pygame.Rect(600, 500, 200, 100)
    pygame.display.flip()
    font = pygame.font.Font(None, 34)
    string_rendered = font.render('ИГРАТЬ', 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect(center=(button_surface.get_width() / 2,
            button_surface.get_height() / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Вызовите функцию on_mouse_button_down()
                if button_rect.collidepoint(event.pos):
                    return
        pygame.draw.rect(button_surface, '#315700', (0, 0, 200, 100))

            # Нарисуйте кнопку на экране
        button_surface.blit(string_rendered, intro_rect)
        screen.blit(button_surface, (button_rect.x, button_rect.y))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

def load_image1(name, colorkey=None):
    fullname = os.path.join('images', name)
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
        image = image.convert()
    return image

def second_screen():
    intro_text = ["ВЫБЕРИТЕ УРОВЕНЬ", "",
                  "1-Й УРОВЕНЬ",
                  "",
                  "2-Й УРОВЕНЬ",
                  "",
                  "3-Й УРОВЕНЬ"]

    fon = pygame.transform.scale(load_image1('mountains1.png'), (1400, 800))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 300
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect(center=(600 / 2, 800))
        text_coord += 10
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    button_surface = pygame.Surface((200, 100))
    button_rect = pygame.Rect(600, 500, 200, 100)
    pygame.display.flip()
    font = pygame.font.Font(None, 34)
    string_rendered = font.render('ИГРАТЬ', 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect(center=(button_surface.get_width() / 2,
                                                  button_surface.get_height() / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)



if __name__ == '__main__':
    global size, screen
    pygame.init()

    n = 5
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    size = 1400, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    start_screen()
    second_screen()

    vrag = Vrag(n)
    step = 10
    # поле 5 на 7
    board = Board(20, 13)
    #board.set_view(800, 300, 60)
    running = True
    n = 5
    all_sprites = pygame.sprite.Group()
    pygame.display.set_caption('Игра')
    vrag = Vrag(n)
    step = 10

    board = Board(13, 13)
    screen.fill((50, 50, 50))
    board.render(screen)

    val = 10
    animation_cooldown = 150
    last_update = pygame.time.get_ticks()
    running = True
    player = Player()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
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
        board.render(screen)
        player.draw()
        vrag.draw()
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()