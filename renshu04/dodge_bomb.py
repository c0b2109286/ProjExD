import pygame as pg
import sys
import random
import math

def main():
    global cx, cy, tori_rect

    tori_img = pg.image.load("fig/0.png")
    tori_img_2X = pg.transform.rotozoom(tori_img, angle=0.0 ,scale=2.0)
    tori_rect = tori_img_2X.get_rect()

    while True:
        pg.display.update()
        screan.fill("BLACK")
        bakudan()
        main_proc()
        tori_rect.center = cx, cy
        screan.blit(tori_img_2X, tori_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT: return
            clock = pg.time.Clock()
            clock.tick(100)

def main_proc():
    global cx, cy
    r = tori_rect.colliderect(image_rect)
    if r == True:
        return

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
    global image_rect
    size = (20, 20)
    image = pg.Surface(size)
    image.get_colorkey()
    pg.draw.circle(image, (255,0,0), (10, 10), 10)
    image_rect = image.get_rect()
    image_rect.center = bx, by
    screan.blit(image, image_rect)
    bakudan_proc()

def bakudan_proc():
    global bx, by, vx, vy
    r = tori_rect.colliderect(image_rect)
    if r == True:
        return

    bx += vx
    by += vy
    check_bound()

def check_bound():
    global cx, cy, bx, by, vx, vy
    if cx < 0:
        cx += 1
    elif cx > 1504:
        cx -= 1
    elif cy < 0:
        cy += 1
    elif cy > 760:
        cy -=1

    if bx <= 0 or bx >= 1580:
        vx *= -1

    elif by <= 0 or by >= 880:
        vy *= -1

if  __name__ == "__main__":
    cx, cy = 900, 400
    bx, by = random.randint(1, 1599), random.randint(1, 899)
    vx, vy = 1,1
    r = False
    pg.init()

    pg.display.set_caption("逃げろ！こうかとん")
    screan = pg.display.set_mode((1600, 900))

    main()

    pg.quit()
    sys.exit()