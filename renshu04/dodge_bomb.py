import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screan = pg.display.set_mode((1600, 900))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
            pg.display.update()

            clock = pg.time.Clock()
            clock.tick(1000)


if  __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()