import pygame as pg
import sys
import random
import math

def main():
    global cx, cy, counter, run, tori_rect, image_rect

    tori_img = pg.image.load("fig/0.png")
    tori_img_2X = pg.transform.rotozoom(tori_img, angle=0.0 ,scale=2.0)
    haikei = pg.image.load("fig/pg_bg.jpg")
    tori_rect = tori_img_2X.get_rect()
    pg.time.set_timer(pg.USEREVENT, 1000)

    while True:
        pg.display.update()
        screan.blit(haikei, (0, 0))
        bakudan()
        main_proc()
        timer()
        tori_rect.center = cx, cy
        screan.blit(tori_img_2X, tori_rect)
        game_over()

        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type == pg.USEREVENT and run==True:
                counter += 1
            if counter not in num_list and counter % 10 == 0 and len(num_list)<=10:
                num_list.append(counter)
                bakudan_place(random.randint(1, 1599), random.randint(1, 899))
            if r == True:
                run = False


def main_proc():
    global cx, cy
    # r = tori_rect.colliderect(image_rect)
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

def bakudan_place(x, y):
    global num
    while True:
        if b_list[num] == False and num <= 10:
            b_list[num] = True
            bx_list[num] = x
            by_list[num] = y

            break
        num += 1

def bakudan():
    global image_rect, r
    n = 0
    for i in b_list:
        if i == True:
            size = (20, 20)
            image = pg.Surface(size)
            pg.draw.circle(image, (255,0,0), (10, 10), 10)
            image_rect = image.get_rect()
            image.set_colorkey((0,0,0))
            image_rect.center = bx_list[n], by_list[n]
            screan.blit(image, image_rect)
            r = tori_rect.colliderect(image_rect)
            n += 1
        else:
            break
    bakudan_proc()

def bakudan_proc():
    global bx_list, by_list, vx_list, vy_list
    # r = tori_rect.colliderect(image_rect)
    if r == True:
        return

    m = 0
    for j in b_list:
        if j == True:
            bx_list[m] += vx_list[m]
            by_list[m] += vy_list[m]
            m += 1
        else:
            break
    check_bound()

def check_bound():
    global cx, cy, m_x, m_y
    if cx < 48:
        cx += 1
    elif cx > 1552:
        cx -= 1
    elif cy < 70:
        cy += 1
    elif cy > 830:
        cy -=1

    q = 0
    for o in b_list:
        if o == True:
            if bx_list[q] < 0 or bx_list[q] > 1580:
                vx_list[q] *= -1
            if by_list[q] < 0 or by_list[q] > 880:
                vy_list[q] *= -1
            q += 1
        else:
            break

def timer():
    font = pg.font.Font("/Windows/Fonts/meiryo.ttc", 80)
    text = font.render(str(counter), True, (255, 255, 255), (0,0,0))
    text.set_colorkey((0, 0, 0))
    screan.blit(text, (60,60))

def game_over():
    if r == True:
        font = pg.font.Font("/Windows/Fonts/meiryo.ttc", 200)
        text = font.render("GAME OVER", True, (255, 55, 0), (0,0,0))
        text.set_colorkey((0, 0, 0))
        screan.blit(text, (200,250))
    

if  __name__ == "__main__":
    cx, cy = 900, 400
    counter = 0
    run = True
    b_list = [False] * 10
    bx_list = [0] * 10
    by_list = [0] * 10
    vx_list = [1] * 10
    vy_list = [1] * 10
    num = 0
    num_list = []
    r = False

    pg.init()

    pg.display.set_caption("逃げろ！こうかとん")
    screan = pg.display.set_mode((1600, 900))
    
    main()

    pg.quit()
    sys.exit()