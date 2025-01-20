import pygame
from pygame.display import update
from screeninfo import get_monitors
import os
import sys
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN
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
        self.idle1 = [load_image(os.path.join('imagi', 'Idle1.png')), load_image(os.path.join('imagi', 'Idle2.png')),
                      load_image(os.path.join('imagi', 'Idle3.png')), load_image(os.path.join('imagi', 'Idle4.png'))]

        # run
        self.run1 = [
                     load_image(os.path.join('imagi', 'Run4.png')),
                     load_image(os.path.join('imagi', 'Run5.png')),
                     load_image(os.path.join('imagi', 'Run6.png')), load_image(os.path.join('imagi', 'Run7.png')),
                     load_image(os.path.join('imagi', 'Run8.png')),
                     load_image(os.path.join('imagi', 'Run9.png'))]
        # atack
        self.atack = [load_image(os.path.join('imagi', 'Attack1.png')), load_image(os.path.join('imagi', 'Attack2.png')),
                      load_image(os.path.join('imagi', 'Attack3.png')), load_image(os.path.join('imagi', 'Attack4.png')),
                      load_image(os.path.join('imagi', 'Attack5.png')), load_image(os.path.join('imagi', 'Attack6.png'))]
        #walk
        self.walk = [load_image(os.path.join('imagi', 'Walk1.png')), load_image(os.path.join('imagi', 'Walk2.png')),
                     load_image(os.path.join('imagi', 'Walk3.png')), load_image(os.path.join('imagi', 'Walk4.png')),
                     load_image(os.path.join('imagi', 'Walk5.png')), load_image(os.path.join('imagi', 'Walk6.png'))]
        #dead
        self.dead = [load_image(os.path.join('imagi', 'Dead1.png')), load_image(os.path.join('imagi', 'Dead2.png')),
                     load_image(os.path.join('imagi', 'Dead3.png')), load_image(os.path.join('imagi', 'Dead4.png')),
                     load_image(os.path.join('imagi', 'Dead5.png')), load_image(os.path.join('imagi', 'Dead6.png')),
                     load_image(os.path.join('imagi', 'Dead7.png')), load_image(os.path.join('imagi', 'Dead8.png'))]

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
        kord = (400, 400)
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
                    elem1 = (elem[0] - self.step, elem[1] + self.step)
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
        id = load_image(os.path.join('imagi', 'grass.png'))
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


if __name__ == '__main__':
    global size, screen
    pygame.init()
    n = 5
    for monitor in get_monitors():
        print(f"{monitor.width}x{monitor.height}")
        x = monitor.width
        y = monitor.height
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    size = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Инициализация игры')
    clock = pygame.time.Clock()
    vrag = Vrag(n)
    step = 10
    # поле 5 на 7
    board = Board(13, 13)
    #board.set_view(800, 300, 60)
    running = True



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        board.render(screen)
        vrag.draw()

        pygame.display.flip()
        clock.tick(10)
    pygame.quit()
