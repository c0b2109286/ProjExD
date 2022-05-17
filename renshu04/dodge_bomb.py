import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screan = pg.display.set_mode((1600, 900))

    tori_img = pg.image.load("fig/0.png")
    tori_img_2X = pg.transform.rotozoom(tori_img, angle=0.0 ,scale=2.0)
    screan.blit(tori_img_2X, (900, 400))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
            pg.display.update()

            clock = pg.time.Clock()
            clock.tick(100)


if  __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()