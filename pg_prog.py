import os
import sys
import pygame
from PIL import Image

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
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top,
                    self.cell_size, self.cell_size), 1)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
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


if __name__ == '__main__':
    pygame.init()
    all_sprites = pygame.sprite.Group()
    size = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Игра')
    board = Board(13, 13)
    screen.fill((50, 50, 50))
    board.render(screen)

    player = Player()
    val = 10
    animation_cooldown = 150
    last_update = pygame.time.get_ticks()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        userInput = pygame.key.get_pressed()
        if pygame.MOUSEBUTTONDOWN:
            player.attack = True
        else:
            player.attack = False
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
        pygame.time.delay(60)
        player.draw()
        pygame.display.flip()