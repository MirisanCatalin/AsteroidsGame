from new_life import NewLife
from constants import *
import pygame
import random

class LifeSpawner:
    def __init__(self, cooldown=5000):  # ms between spawns
        self.cooldown = cooldown
        self.last_spawn_time = 0

    def try_spawn(self, now, all_sprites, life_group):
        # Only spawn if enough time passed and none exist
        if now - self.last_spawn_time >= self.cooldown and len(life_group) == 0:
            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(50, SCREEN_HEIGHT - 50)
            new_life = NewLife(x, y, radius=20)
            all_sprites.add(new_life)
            life_group.add(new_life)
            self.last_spawn_time = now

