import pygame as pg
import sys
import random

class Screan(pg.sprite.Sprite):       #Screenクラス（スクリーン描写）

    def __init__(self, fn = "fig/pg_bg.jpg", width = 1600, height = 900, title = "逃げろ！こうかとん"):
        self.width = width
        self.height = height
        pg.display.set_caption(title)
        self.disp = pg.display.set_mode((self.width, self.height))      #ウィンドウ作成（1600, 900）surface
        self.rect = self.disp.get_rect()        #Rect
        self.image = pg.image.load(fn)      #背景画像

class Bird(pg.sprite.Sprite):       #Birdクラス（とり描写）
    key_data = {"K_UP":-1, "K_DOWN":1, "K_LEFT":-1, "K_RIGHT":1}

    def __init__(self, tori_name, rate, x, y):
        # rate：拡大率, rate :  
        super().__init__()
        self.image = pg.transform.rotozoom(pg.image.load(tori_name), angle=0, scale=rate)           #とり画像の拡大
        self.rect = self.image.get_rect()       #Rect取得
        self.rect.center = x, y

        
    def update(self):       #こうかとんが外に出ないようにする関数
        key = pg.key.get_pressed()          #押されたキーを取得

        if key[pg.K_UP]:
            self.rect.centery += int(Bird.key_data["K_UP"])
        elif key[pg.K_DOWN]:
            self.rect.centery += int(Bird.key_data["K_DOWN"])
        elif key[pg.K_LEFT]:
            self.rect.centerx += int(Bird.key_data["K_LEFT"])
        elif key[pg.K_RIGHT]:
            self.rect.centerx += int(Bird.key_data["K_RIGHT"])

        if self.rect.centerx  < 0:
            self.rect.centerx += 1
        elif self.rect.centerx  > 1500:
            self.rect.centerx  -= 1
        elif self.rect.centery < 0:
            self.rect.centery += 1
        elif self.rect.centery > 770:
            self.rect.centery -=1

class Bomb(pg.sprite.Sprite):
    def __init__(self, color, hankei, speed_x, speed_y, screen):
        # hakei : ボールの半径, speed_x : ｘ方向へのボールの速さ , speed_y : ｘ方向へのボールの速さ, screen : screenオブジェクト
        super().__init__()
        self.image = pg.Surface((20, 20))
        pg.draw.circle(self.image , color, (10, 10), hankei)
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.rect.centerx =   random.randint(0, screen.rect.width)           #爆弾のｘ座標（ランダム）
        self.rect.centery =   random.randint(0, screen.rect.height)          #爆弾のｙ座標（ランダム）
        self.vx = speed_x
        self.vy = speed_y

    def update(self):
        self.rect.move_ip(self.vx, self.vy)

        if self.rect.centerx < 0 or self.rect.centerx > 1580:
            self.vx *= -1           #ボールの進む向き反転
        if self.rect.centery < 0 or self.rect.centery > 880:
            self.vy *= -1           #ボールの進む向き反転

def main():
    screan = Screan()       #コンストラクタを呼び出す
    bird = Bird("fig/6.png", 2, 900, 400)
    bomb = Bomb((255, 0, 0), 10, 1, 1, screan)

    bombs = pg.sprite.Group()
    for _ in range(5):
        bombs.add( Bomb((255, 0, 0), 10, 1, 1, screan) )

    while True:
        pg.display.update()
        screan.disp.blit(screan.image, (0,0))       #背景画像の貼り付け (0, 0)

        screan.disp.blit(bird.image, bird.rect)     #とり画像の貼り付け
        bird.update()                               #とり座標のアップデート
        
        #screan.disp.blit(bomb.image, bomb.rect)     #爆弾画像の貼り付け
        bombs.update()                               #爆弾座標のアップデート
        bombs.draw(screan.disp)                          


        if pg.sprite.collide_rect(bird, bomb):        #とりが爆弾に衝突したとき
            return                                  #whileを抜ける

        for event in pg.event.get():
            if event.type == pg.QUIT: return        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()