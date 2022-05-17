import pygame as pg
import sys
import random
import math

def main():
    global cx, cy

    tori_img = pg.image.load("fig/0.png")
    tori_img_2X = pg.transform.rotozoom(tori_img, angle=0.0 ,scale=2.0)

    while True:
        pg.display.update()
        main_proc()
        screan.fill("BLACK")
        bakudan()
        bakudan_proc()
        screan.blit(tori_img_2X, (cx, cy))

        for event in pg.event.get():
            if event.type == pg.QUIT: return
            clock = pg.time.Clock()
            clock.tick(100)

def main_proc():
    global cx, cy
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        cy -= 1
    elif key[pg.K_DOWN]:
        cy += 1
    elif key[pg.K_LEFT]:
        cx -= 1
    elif key[pg.K_RIGHT]:
        cx += 1

def bakudan():
    size = (20, 20)
    image = pg.Surface(size)
    image.get_colorkey()
    pg.draw.circle(image, (255,0,0), (10, 10), 10)
    screan.blit(image, (bx, by))

def bakudan_proc():
    global bx, by
    vx = 1
    vy = 1
    bx += vx
    by += vy
    

if  __name__ == "__main__":
    cx, cy = 900, 400
    bx, by = random.randint(1, 1599), random.randint(1, 899)
    pg.init()

    pg.display.set_caption("逃げろ！こうかとん")
    screan = pg.display.set_mode((1600, 900))

    main()

    pg.quit()
    sys.exit()
