from tkinter import Canvas
import pygame as pg
import sys

def main():
    global cx, cy

    pg.display.set_caption("逃げろ！こうかとん")
    screan = pg.display.set_mode((1600, 900))
    

    tori_img = pg.image.load("fig/0.png")
    tori_img_2X = pg.transform.rotozoom(tori_img, angle=0.0 ,scale=2.0)
    

    while True:
        pg.display.update()
        main_proc()
        screan.fill("BLACK")
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
    

if  __name__ == "__main__":
    cx, cy = 900, 400
    pg.init()
    main()
    pg.quit()
    sys.exit()
    