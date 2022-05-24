from cmath import rect
from turtle import width
import pygame as pg
import sys
import random

class Screan:       #Screenクラス（スクリーン描写）

    def __init__(self, fn = "fig/pg_bg.jpg", width = 1600, height = 900, title = "逃げろ！こうかとん"):
        self.width = width
        self.height = height
        pg.display.set_caption(title)
        self.disp = pg.display.set_mode((self.width, self.height))      #ウィンドウ作成（1600, 900）surface
        self.rect = self.disp.get_rect()        #Rect
        self.image = pg.image.load(fn)      #背景画像

class Bird:       #Birdクラス（とり描写）
    key_data = {"K_UP":-1, "K_DOWN":1, "K_LEFT":-1, "K_RIGHT":1}

    def __init__(self, tori_name = "fig/6.png", rate = 2, x = 900, y = 400):
        # rate：拡大率
        self.x = x        #とりのｘ座標
        self.y = y        #とりのｙ座標
        self.image = pg.transform.rotozoom(pg.image.load(tori_name), angle=0, scale=rate)           #とり画像の拡大
        self.rect = self.image.get_rect()       #Rect取得

        
    def update(self):
        key = pg.key.get_pressed()          #押されたキーを取得

        if key[pg.K_UP]:
            self.y += int(Bird.key_data["K_UP"])
        elif key[pg.K_DOWN]:
            self.y += int(Bird.key_data["K_DOWN"])
        elif key[pg.K_LEFT]:
            self.x += int(Bird.key_data["K_LEFT"])
        elif key[pg.K_RIGHT]:
            self.x += int(Bird.key_data["K_RIGHT"])

        if self.x < 0:
            self.x += 1
        elif self.x > 1500:
            self.x -= 1
        elif self.y < 0:
            self.y += 1
        elif self.y > 770:
            self.y -=1



def main():
    screan = Screan()       #コンストラクタを呼び出す
    bird = Bird()

    while True:
        pg.display.update()
        screan.disp.blit(screan.image, (0,0))       #背景画像の貼り付け (0, 0)
        bird.rect.center = bird.x, bird.y
        screan.disp.blit(bird.image, bird.rect)
        bird.update()

        for event in pg.event.get():
            if event.type == pg.QUIT: return        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()