from pg_screen import *


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

