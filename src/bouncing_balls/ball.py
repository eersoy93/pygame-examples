
import pygame
import random

class Ball:
    def __init__(self, name, filepath):
        self.name = name
        self.filepath = filepath

        self.image = pygame.image.load(self.filepath)
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 512)
        self.rect.y = random.randint(0, 512)

        self.speed = [random.choice([-2, 2]), random.choice([-2, 2])]

    def get_image(self):
        return self.image

    def get_name(self):
        return self.name

    def get_rectangle(self):
        return self.rect

    def get_speed(self):
        return self.speed

    def set_rect(self, rect):
        self.rect = rect