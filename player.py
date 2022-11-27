import pygame as pg
from settings import *
from entity import Entity

JUMP_FORCE: int = 0.005
MAX_SPEED: float = 0.8
MIN_SPEED: float = -0.8


class Player(Entity):
    def __init__(self, groups: list, pos: pg.math.Vector2):
        super(Player, self).__init__(groups, pg.image.load('./imgs/New Piskel-1.png'), pos)
        self.speed: pg.math.Vector2 = pg.math.Vector2()

    def input_(self, delta_time: int):
        key: pg.key.ScancodeWrapper = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self.speed.y -= JUMP_FORCE * delta_time

    def physics(self, delta_time: int):
        self.speed.y += GRAVITY * delta_time

        if self.speed.y >= MAX_SPEED:
            self.speed.y = MAX_SPEED
        elif self.speed.y <= MIN_SPEED:
            self.speed.y = MIN_SPEED

    def update(self, delta_time: int):
        print(self.speed.y)
        self.input_(delta_time)
        self.physics(delta_time)
        self.rect.topleft += self.speed * delta_time
