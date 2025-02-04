import pygame
from PIL import Image
import os
import sys
import pygame
import datetime as dt
from random import randint

size = 1400, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Игра')
screen.fill((50, 50, 50))

n = 5
step = 10
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
clock = pygame.time.Clock()

val = 10
animation_cooldown = 150
uron_zomb = 10
uron_igr = 10
boss_uron = 50
last_update = pygame.time.get_ticks()


jisn_igr = 300
jisn_zomb = 400
running = True

n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
n6 = 6
n7 = 7
n8 = 8
n9 = 9
n11 = 10
n12 = 11
n13 = 12
n14 = 13
n15 = 14
step = 10

volna = 0
poln = 0