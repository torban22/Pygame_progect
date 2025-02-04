from pg_screen import *

class Sword(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.x = 350
        self.y = 350
        self.rect = pygame.Rect(0, 0, 100, 100)

    def draw(self):
        self.x, self.y = player.get_pos()