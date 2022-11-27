import pygame as pg
from settings import *


class Entity(pg.sprite.Sprite):
    def __init__(self, groups: list, image: pg.Surface, pos: pg.math.Vector2):
        super(Entity, self).__init__(groups)
        self.image: pg.Surface = image
        self.rect: pg.Rect = self.image.get_rect(topleft=pos)
