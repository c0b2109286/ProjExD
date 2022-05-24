import pygame as pg
import sys

class Screan:
    def __init__(self, haikei_name = "fig/pg_bg.jpg", width = 1600, height = 900, title_name = "逃げろ！こうかとん"):
        self.width = width
        self.height = height
        self.disp = pg.display.set_mode((self.width, self.height))
        self.rect = self.disp.get_rect()
        self.image = pg.image.load(haikei_name)


def main():
    screan = Screan()

    while True:
        pg.display.update()
        screan.disp.blit(screan.image, (0,0))

        for event in pg.event.get():
            if event.type == pg.QUIT: return        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()