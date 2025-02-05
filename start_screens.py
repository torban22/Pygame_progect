from pg_screen import *


LEVEL = 0

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
    pygame.mixer.music.load(os.path.join('sounds', 'Magical Forest.wav'))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)

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
                    sound1 = pygame.mixer.Sound(os.path.join('sounds', 'btn.mp3'))
                    sound1.play()
                    sound1.set_volume(0.2)
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
    global LEVEL
    intro_text = ["ВЫБЕРИТЕ УРОВЕНЬ", "",
                  "1-Й УРОВЕНЬ",
                  "",
                  "2-Й УРОВЕНЬ",
                  "",
                  "3-Й УРОВЕНЬ"]

    fon = pygame.transform.scale(load_image1('mountains1.png'), (1400, 800))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 320
    for i in range(len(intro_text)):
        string_rendered = font.render(intro_text[i], 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect(center=(600 / 2, 800))
        text_coord += 10
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    button_surface1 = pygame.Surface((320, 75))
    button_rect1 = pygame.Rect(100, 400, 320, 75)
    pygame.display.flip()
    string_rendered1 = font.render('1-Й УРОВЕНЬ', 1, pygame.Color('white'))
    intro_rect1 = string_rendered1.get_rect(center=(button_surface1.get_width() / 2,
                                                  button_surface1.get_height() / 2))
    button_surface2 = pygame.Surface((320, 75))
    button_rect2 = pygame.Rect(100, 500, 320, 75)
    pygame.display.flip()
    font = pygame.font.Font(None, 50)
    string_rendered2 = font.render('2-Й УРОВЕНЬ', 1, pygame.Color('white'))
    intro_rect2 = string_rendered2.get_rect(center=(button_surface2.get_width() / 2,
                                                  button_surface2.get_height() / 2))
    button_surface3 = pygame.Surface((320, 75))
    button_rect3 = pygame.Rect(100, 600, 320, 75)
    pygame.display.flip()
    font = pygame.font.Font(None, 50)
    string_rendered3 = font.render('3-Й УРОВЕНЬ', 1, pygame.Color('white'))
    intro_rect3 = string_rendered3.get_rect(center=(button_surface3.get_width() / 2,
                                                  button_surface3.get_height() / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect1.collidepoint(event.pos):
                    sound2 = pygame.mixer.Sound(os.path.join('sounds', 'btn.mp3'))
                    sound2.play()
                    sound2.set_volume(0.2)
                    LEVEL = 1
                    return
                if button_rect2.collidepoint(event.pos):
                    sound2 = pygame.mixer.Sound(os.path.join('sounds', 'btn.mp3'))
                    sound2.play()
                    sound2.set_volume(0.2)
                    LEVEL = 2
                    return
                if button_rect3.collidepoint(event.pos):
                    sound2 = pygame.mixer.Sound(os.path.join('sounds', 'btn.mp3'))
                    sound2.play()
                    sound2.set_volume(0.2)
                    LEVEL = 3
                    return
        pygame.draw.rect(button_surface1, '#315700', (0, 0, 320, 75))
        pygame.draw.rect(button_surface2, '#315700', (0, 0, 320, 75))
        pygame.draw.rect(button_surface3, '#315700', (0, 0, 320, 75))

        # Нарисуйте кнопку на экране
        button_surface1.blit(string_rendered1, intro_rect1)
        button_surface2.blit(string_rendered2, intro_rect2)
        button_surface3.blit(string_rendered3, intro_rect3)
        screen.blit(button_surface1, (button_rect1.x, button_rect1.y))
        screen.blit(button_surface2, (button_rect2.x, button_rect2.y))
        screen.blit(button_surface3, (button_rect3.x, button_rect3.y))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

def lose_screen():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join('sounds', 'game_over.mp3'))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)
    size = 1400, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Игра')
    screen.fill((50, 50, 50))
    fon = pygame.transform.scale(load_image1('game_over.jpg'), (1400, 800))
    screen.blit(fon, (0, 0))
    cur_time = pygame.time.get_ticks()
    last = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and cur_time - last >= 8000:
                return
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
        cur_time = pygame.time.get_ticks()

def win_screen():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join('sounds', 'victory.mp3'))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)
    size = 1400, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Игра')
    screen.fill((50, 50, 50))
    fon = pygame.transform.scale(load_image1('win.webp'), (1400, 800))
    screen.blit(fon, (0, 0))
    cur_time = pygame.time.get_ticks()
    last = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and cur_time - last >= 2000:
                print(cur_time - last, 'время')
                return
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
        cur_time = pygame.time.get_ticks()

def see_points():
    global LEVEL
    from pg_player import player
    print(player.point_now)
    size = 1400, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Игра')
    screen.fill('black')
    print(LEVEL)
    font = pygame.font.Font(None, 50)
    if LEVEL == 1:
        with open('levels/level1.txt', 'r') as f:
            txt = [float(i) for i in f.read().split(';')]
            print(txt)
        f.close()
        if round(player.point_now, 1) > txt[0]:
            txt[0] = round(player.point_now, 1)
        with open('levels/level1.txt', 'w') as f:
            f.write(';'.join(map(str, txt)))
        f.close()
    elif LEVEL == 2:
        with open('levels/level2.txt', 'r') as f:
            txt = [float(i) for i in f.read().split(';')]
            print(txt)
        f.close()
        if round(player.point_now, 1) > txt[0]:
            txt[0] = round(player.point_now, 1)
        with open('levels/level2.txt', 'w') as f:
            f.write(';'.join(map(str, txt)))
        f.close()
    elif LEVEL == 3:
        with open('levels/level3.txt', 'r') as f:
            txt = [float(i) for i in f.read().split(';')]
            print(txt)
        f.close()
        if round(player.point_now, 1) > txt[0]:
            txt[0] = round(player.point_now, 1)
        with open('levels/level3.txt', 'w') as f:
            f.write(';'.join(map(str, txt)))
        f.close()
    else:
        txt = [0, 0]
    string_rendered = font.render(f'Набранные вами очки: {str(round(player.point_now, 1))}', 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect(center=(700, 200))
    screen.blit(string_rendered, intro_rect)
    string_rendered = font.render(f'Ваш рекорд: {str(txt[0])}', 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect(center=(700, 400))
    screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)



