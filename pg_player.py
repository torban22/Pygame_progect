from pg_screen import *
class Sword(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.x = 350
        self.y = 350
        self.rect = pygame.Rect(0, 0, 100, 100)


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
        self.k = 100
        self.point_now = 0

        self.health = 1000
        self.attack = False
        self.time_start = dt.datetime.now()
        self.last_time = dt.datetime.now()

        self.sword = Sword()

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
        self.attack_up = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'attack1', 'attack1Up.gif'))
        self.attack_right = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'attack1', 'attack1Right.gif'))
        self.attack_left = split_animated_gif(os.path.join('images', 'player', 'knight', 'GIFs', 'attack1', 'attack1Left.gif'))

        self.draw()
        self.image = self.idle_down[0]
        self.rect = self.image.get_rect()
        self.mask_play = pygame.mask.from_surface(self.image)



    def draw(self):
        global last_update, animation_cooldown
        self.imp = None
        cur_time = pygame.time.get_ticks()
        if self.step >= 3:
            self.step = 0
            if self.attack:
                self.attack = False
        if cur_time - last_update >= animation_cooldown:
            self.step += 1
            last_update = cur_time
        if self.down and self.attack:
            self.imp = self.attack_down[self.step]
        elif self.up and self.attack:
            self.imp = self.attack_up[self.step]
        elif self.right and self.attack:
            self.imp = self.attack_right[self.step]
        elif self.left and self.attack:
            self.imp = self.attack_left[self.step]
        elif self.down and self.move is False:
            self.imp = self.idle_down[self.step]
        elif self.right and self.move is False:
            self.imp = self.idle_right[self.step]
        elif self.left and self.move is False:
            self.imp = self.idle_left[self.step]
        elif self.up and self.move is False:
            self.imp = self.idle_up[self.step]
        elif self.down and self.move:
            self.imp = self.run_down[self.step]
        elif self.right and self.move:
            self.imp = self.run_right[self.step]
        elif self.left and self.move:
            self.imp = self.run_left[self.step]
        elif self.up and self.move:
            self.imp = self.run_up[self.step]
        if self.imp:
            self.rect = self.imp.get_rect()
            self.mask = pygame.mask.from_surface(self.imp)
        self.draw_health()
        pygame.draw.circle(screen, 'red', (self.x + 25, self.y + 25), 50)
        self.sword.mask = pygame.mask.from_surface(pygame.Surface((100, 100)))


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
        return [(self.x + 25) // 60, (self.y + 25) // 60]

    def draw_health(self):
        pygame.draw.rect(screen, 'green', (10, 10, self.health, 30))
        pygame.display.flip()

    def get_hurt(self):
        if self.health > 0:
            self.health -= uron_zomb

    def points(self):
        difference = dt.datetime.now() - self.time_start
        print(difference.seconds)
        self.k = 100 / difference.seconds
        self.point_now += self.k
        self.last_time = dt.datetime.now()



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

player = Player()
mask_play = player.mask_play