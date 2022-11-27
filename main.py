import pygame as pg
import sys
from player import Player
from settings import *


class Game:
    def __init__(self):
        self.screen: pg.Surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_NAME)

        self.visible_sprites: pg.sprite.Group = pg.sprite.Group()

        Player([self.visible_sprites], (SCREEN_WIDTH / 16, 0))

    def run(self):
        clock: pg.time.Clock = pg.time.Clock()
        while True:
            delta_time: int = clock.tick(FPS)
            Game.handle_events()
            self.visible_sprites.update(delta_time)
            self.render()

    def render(self):
        self.screen.fill('black')
        self.visible_sprites.draw(self.screen)
        pg.display.update()

    @staticmethod
    def handle_events():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

if __name__ == '__main__':
    Game().run()
