'''from pg_player import player, mask_play
from pg_screen import *


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
        #self.add(group)
        mask_enem = pygame.mask.from_surface(self.image[0])

        self.frame = 0  # текущий кадр
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 10  # как быстро кадры меняются


    def poisk(self):
        b = (randint(100, 700), randint(50, 100))
        return b


    def draw(self, ind):
        global ofset, jisn_igr, jisn_zomb, running, numb
        self.draw_health()
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
            print('KKGJGJGJFJG')
            self.move = False

            self.num = self.indik
            print(f'номер с кем столкнулся {self.num}')
            pygame.time.set_timer(pygame.USEREVENT, 100, True)
            if self.health <= 0:
                self.jisn = False
            #print(jisn_igr)

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
                #print(self.frame)
                if self.frame == 4:
                    running = False
                    pygame.time.wait(10)
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
    return ret'''

from pg_player import player, mask_play
from pg_screen import *


class Vrag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        global mask_enem
        self.koords = []
        self.step = 2
        self.health = 400
        cor = self.poisk()
        self.num = 0
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
        #self.add(group)
        mask_enem = pygame.mask.from_surface(self.image[0])

        self.frame = 0  # текущий кадр
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 10  # как быстро кадры меняются


    def poisk(self):
        b = (randint(100, 700), randint(50, 100))
        return b


    def draw(self, ind):
        global ofset, jisn_igr, jisn_zomb, running, numb
        self.draw_health()
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
            print('KKGJGJGJFJG')
            self.move = False

            self.num = ind
            print(f'номер с кем столкнулся {self.num}')
            pygame.time.set_timer(pygame.USEREVENT, 100, True)
            if self.health <= 0:
                self.jisn = False
            #print(jisn_igr)

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
                #print(self.frame)
                if self.frame == 4:
                    running = False
                    pygame.time.wait(10)
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