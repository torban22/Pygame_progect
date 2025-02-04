from pg_player import player, mask_play
from pg_screen import *



class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        #global mask_enem
        self.koords = []
        #self.indik  = n
        self.step = 2
        self.health = 600
        cor = self.poisk()
        self.num = 0
        self.koords = cor
        self.end = False



        # idle
        self.idle1 = [load_image(os.path.join('images', 'boss',  'Idle1.png')), load_image(os.path.join('images', 'boss',  'Idle2.png')),
                      load_image(os.path.join('images', 'boss',  'Idle3.png')), load_image(os.path.join('images', 'boss',  'Idle4.png'))]

        # run
        self.run1 = [
                     load_image(os.path.join('images', 'boss',  'Run4.png')),
                     load_image(os.path.join('images', 'boss',  'Run5.png')),
                     load_image(os.path.join('images', 'boss',  'Run6.png')), load_image(os.path.join('images', 'boss', 'Run7.png')),
                     load_image(os.path.join('images', 'boss',  'Run8.png')),
                     load_image(os.path.join('images', 'boss',  'Run9.png'))]
        # atack
        self.atack = [load_image(os.path.join('images', 'boss',  'Attack1.png')), load_image(os.path.join('images', 'boss', 'Attack2.png')),
                      load_image(os.path.join('images', 'boss',  'Attack3.png')), load_image(os.path.join('images', 'boss', 'Attack4.png')),
                      load_image(os.path.join('images', 'boss',  'Attack5.png')), load_image(os.path.join('images', 'boss', 'Attack6.png'))]
        #walk
        self.walk = [load_image(os.path.join('images', 'boss',  'Walk1.png')), load_image(os.path.join('images', 'boss', 'Walk2.png')),
                     load_image(os.path.join('images', 'boss',  'Walk3.png')), load_image(os.path.join('images', 'boss', 'Walk4.png')),
                     load_image(os.path.join('images', 'boss',  'Walk5.png')), load_image(os.path.join('images', 'boss', 'Walk6.png'))]
        #dead
        self.dead = [load_image(os.path.join('images', 'boss',  'Dead1.png')), load_image(os.path.join('images', 'boss', 'Dead2.png')),
                     load_image(os.path.join('images', 'boss',  'Dead3.png')), load_image(os.path.join('images', 'boss', 'Dead4.png')),
                     load_image(os.path.join('images', 'boss',  'Dead5.png')), load_image(os.path.join('images', 'boss', 'Dead6.png')),
                     load_image(os.path.join('images', 'boss',  'Dead7.png')), load_image(os.path.join('images', 'boss',  'Dead8.png'))]
        self.image = self.run1[0]
        self.move = True
        self.jisn = True
        self.rect = self.image[0].get_rect()
        self.mask_boss = pygame.mask.from_surface(self.image[0])
        #self.add(group)
        #mask_enem = pygame.mask.from_surface(self.image[0])

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
        self.draw_health()
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
        if mask_play.overlap_area(self.mask_boss, ofset) > 0:
            self.move = False
            player.boss = True
            #NUM = self.indik
            #print(f'номер с кем столкнулся {NUM}')
            if player.attack and player.health >= 0:
                self.get_hurt()
            pygame.time.set_timer(pygame.USEREVENT, 100, True)
            if self.health <= 0:
                self.jisn = False
            #print(jisn_igr)

        elif not mask_play.overlap_area(self.mask_boss, ofset) > 0:
            self.move = True

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
