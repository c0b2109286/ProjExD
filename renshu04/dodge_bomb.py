import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screan = pg.display.set_mode((1600, 900))

    clock = pg.time.Clock()
    clock.tick(1)

if  __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()