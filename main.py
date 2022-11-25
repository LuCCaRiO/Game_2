import pygame as pg
import sys
from settings import *


class Game:
    def __init__(self):
        self.screen: pg.Surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.RESIZABLE)
        pg.display.set_caption(GAME_NAME)

    def run(self):
        clock: pg.time.Clock = pg.time.Clock()
        while True:
            clock.tick(FPS)
            Game.handle_events()
            self.render()

    def render(self):
        self.screen.fill('black')
        pg.display.update()

    @staticmethod
    def handle_events():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

if __name__ == '__main__':
    Game().run()
