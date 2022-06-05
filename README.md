# プロジェクト演習I・テーマD
## 第6回
### Pygameでゲーム実装
#### 基本機能
- ゲーム概要：
    - rensyu06/dodge_bomb.pyを実行すると，1600x900のスクリーンが描画される。初めの画面はスタート画面でスペースキーを押してスタート。次の画面はプレイ画面で、自分のマレット（エアホッケーで使うボールをはじくための道具）を動かして、画面上のボールをはじき相手のゴールを狙うゲーム。最後の画面は結果画面で、得点を勝った方の名前を表示。
    - 制限時間は60秒
    - 制限時間と得点は画面上部に記載
    - ボールは10秒ごとに一つ増加する
    - ゴール、マレット、壁にあたった時に効果音が鳴る。効果音はそれぞれ異なる。
    - ゲームを行うには二人必要で、一人はキーボードのw,a,s,d、もう一人は矢印キーを使ってマレットを動かし戦う。
- 操作方法：一人はキーボードのw,a,s,d、もう一人は矢印キーを用いる。
- プログラムの説明:
    - dodge_bomb.pyをコマンドラインから実行すると，pygameの初期化，main関数の順に処理が進む
    - Screanクラス: スクリーンの詳細設定のクラス
    - Malletクラス: マレットの詳細設定と移動、画面外へでないようにするためのクラス
    - Enemyクラス: Enemyマレットの詳細設定と移動、画面外へ出ないようにするためのクラス。Mallet クラスとは移動のための用いるキーが異なる。
    - Ballクラス:ボールの詳細設定と画面外に出ないようにするためのクラス
    - Goalクラス:ゴールの詳細設定のクラス
    - main関数では，スクリーンの生成，ゴール描写用のコンテナ，ボール描写用のコンテナ, マレット描写用コンテナの作成、を行う
    - main関数の無限ループでは場面転換、ボールの描画、ゴールの描写、マレットの描写、ボールとマレットの当たり判定、ゴールとマレットの当たり判定、得点、制限時間の描写を行う

#### TODO
- コンテニュー機能
- 勝利数の記録

#### メモ
import pygame as pg
import sys

class Screan(pg.sprite.Sprite):

    def __init__(self, width, height, title):
        # width:画面の横サイズ, height:画面の縦のサイズ
        super().__init__()
        self.width, self.height = width, height
        pg.display.set_caption(title)
        self.disp = pg.display.set_mode((self.width, self.height))

class Mallet(pg.sprite.Sprite):         #マレットを描画するためのクラス

    def __init__(self, mx, my, size, color):
        # mx:自分のマレットのｘ座標, my:自分のマレットのｙ座標, size:マレットのサイズ, color:マレットの色
        super().__init__()
        self.image = pg.Surface((size, size))
        pg.draw.rect(self.image, color, (0, 0, size, size))
        self.rect = self.image.get_rect()       #rect取得
        self.rect.center = mx, my
    
    def update(self):
        key = pg.key.get_pressed()          #押されたキーを取得

        if key[pg.K_UP]:
            self.rect.centery -= 1
        elif key[pg.K_DOWN]:
            self.rect.centery += 1
        elif key[pg.K_LEFT]:
            self.rect.centerx -= 1
        elif key[pg.K_RIGHT]:
            self.rect.centerx += 1
    
        if self.rect.centerx  < 0:
            self.rect.centerx += 1
        elif self.rect.centerx  > 1600:
            self.rect.centerx  -= 1
        elif self.rect.centery < 0:
            self.rect.centery += 1
        elif self.rect.centery > 900:
            self.rect.centery -=1

class Enemy(pg.sprite.Sprite):      #敵のマレットを描画するためのクラス

    def __init__(self, ex, ey, size, color):
        # mx:敵のマレットのｘ座標, my:敵のマレットのｙ座標, size:マレットのサイズ, color:マレットの色
        super().__init__()
        self.image = pg.Surface((size, size))
        pg.draw.rect(self.image, color, (0, 0, size, size))
        self.rect = self.image.get_rect()       #rectを取得
        self.rect.center = ex, ey

    def update(self):       #敵のマレットの動作と画面外に出ないようにする
        key = pg.key.get_pressed()          #押されたキーを取得

        if key[pg.K_w]:
            self.rect.centery -= 1
        elif key[pg.K_s]:
            self.rect.centery += 1
        elif key[pg.K_a]:
            self.rect.centerx -= 1
        elif key[pg.K_d]:
            self.rect.centerx += 1
    
        if self.rect.centerx  < 0:
            self.rect.centerx += 1
        elif self.rect.centerx  > 1600:
            self.rect.centerx  -= 1
        elif self.rect.centery < 0:
            self.rect.centery += 1
        elif self.rect.centery > 900:
            self.rect.centery -=1

class Ball(pg.sprite.Sprite):       #ボールを描画するためのクラス

    def __init__(self, bx, by, vx, vy, size, color, sounds):
        # bx:ボールのｙ座標, by:ボールのx座標,vx:ボール（ｘ方向）進む速さ,vy:ボール（ｙ方向）に進む速さ,sounds:bgmのリスト
        super().__init__()
        self.image = pg.Surface((size, size))              #sizeの大きさのsurfaceを用意
        pg.draw.circle(self.image, color,(size/2, size/2), size/2)      #surface上に円を描写
        self.rect = self.image.get_rect()             #rect取得
        self.image.set_colorkey((0,0,0))
        self.rect.center = bx, by
        self.vx, self.vy = vx, vy
        self.sounds = sounds

    def update(self):      #ballが画面外に出ないようにする
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.centerx < 0 or self.rect.centerx > 1580:
            self.vx *= -1
            self.sounds[0].play()
        if self.rect.centery < 0 or self.rect.centery > 860:
            self.vy *= -1
            self.sounds[0].play()

class Goal(pg.sprite.Sprite):         #ゴールを描画するためのクラス
    def __init__(self, gx, gy, size, color, score, num):
        super().__init__()
        self.image = pg.Surface((10, size))
        pg.draw.rect(self.image, color, (0, 0, 10, size))
        self.rect = self.image.get_rect()       #rect取得
        self.rect.center = gx, gy
        self.score = score
        self.num = num

def main():
    font_score, font_time, font_text_one, font_text_two = pg.font.Font(None, 150), pg.font.Font(None, 200), \
                                                            pg.font.Font(None, 350), pg.font.Font(None, 250)     #使用するフォント
    ball_num = []       #ボールが追加された時間を保持するリストの初期化
    screan_num = 0      #スタート画面、プレイ画面、結果画面切り替え用numの初期化
    time = 60            #時間の初期化
    pg.time.set_timer(pg.USEREVENT, 1000)
    sounds = [pg.mixer.Sound("oto/ball.wav"), pg.mixer.Sound("oto/bgm1.wav"),  pg.mixer.Sound("oto/goal1.wav"),  \
                pg.mixer.Sound("oto/goal2.wav"),  pg.mixer.Sound("oto/mallet.wav"), pg.mixer.Sound("oto/start.wav")]        #BGM、効果音のリスト

    screan = Screan(1600, 900, "ホッケー")

    mallets = pg.sprite.Group()           #マレット用のコンテナの作成
    mallets.add(Mallet(1200, 400, 70, (0, 200, 255)), Enemy(400, 400, 70, (255, 0, 0)))
    #コンテナにマレットを二つ（自分と敵）を追加
    
    goals = pg.sprite.Group()      #ゴール用のコンテナ作成
    goals.add(Goal(5, 450, 400, (255,0, 0), 0, 0), Goal(1595, 450, 400, (0, 200, 255), 0, 1))
    #コンテナにゴールを二つ追加

    ball_group = pg.sprite.Group()      #ボール用コンテナの作成

    while True:
        key = pg.key.get_pressed()      #押されたキーを取得

        if screan_num == 0:
            pg.display.update()
            screan.disp.fill((0,0,0))
            screan.disp.blit(font_text_one.render("START", True, (0, 255, 0)), [20, 150])
            screan.disp.blit(font_text_two.render("---> PUSH : Space", True, (0, 255, 0)), [80, 600])

            if key[pg.K_SPACE]:         #spaceキーが押されたとき
                sounds[5].play()        #効果音を再生
                screan_num =1           #screan_numを1にして場面転換

            for event in pg.event.get():
                if event.type == pg.QUIT: return

        if screan_num == 1:
            pg.display.update()
            screan.disp.fill((0,0,0))

            goals.draw(screan.disp)         #ゴールを描写

            mallets.update()                #malletsのupdateを実行
            mallets.draw(screan.disp)       #malletsを描写

            ball_group.update()             #ball_groupのupdateを実行
            ball_group.draw(screan.disp)    #ball_groupを描写


            #ボールとマレットの衝突判定
            for mallet in mallets:              #マレット用のコンテナから一つずつ取り出す
                for ball in ball_group:         #ボール用コンテナから一つずつ取り出す
                    if pg.sprite.collide_rect(mallet, ball):
                        if ball.rect.centerx >= mallet.rect.centerx + 35 or ball.rect.centerx <= mallet.rect.centerx - 35:
                            ball.vx *= -1
                            sounds[4].play()
                        if ball.rect.centery >= mallet.rect.centery + 35 or ball.rect.centery <= mallet.rect.centery - 35:
                            ball.vy *= -1
                            sounds[4].play()

            #ゴールとボールの衝突判定と得点の増加を行う
            for goal in goals:                  #ゴール用のコンテナから一つずつ取り出す
                for ball in ball_group:         #ボール用のコンテナから一つずつ取り出す
                    if pg.sprite.collide_rect(goal, ball):
                        if ball.rect.centerx >= goal.rect.centerx + 5 or ball.rect.centerx <= goal.rect.centerx - 5:
                            ball.vx *= -1
                            goal.score += 1         #得点を追加
                            if goal.num == 1: sounds[2].play()
                            else:sounds[3].play()
                                
                        if ball.rect.centery >= goal.rect.centery + 200 or ball.rect.centery <= goal.rect.centery - 200:
                            ball.vy *= -1
                            sounds[2].play()
            
            #得点の表示を行う
            for goal in goals:
                if goal.num == 1:       #どちらのゴール化を判定
                    text = font_score.render(str(goal.score), True, (255, 0, 0))
                    screan.disp.blit(text, [200, 20])
                    goal1_score = goal.score
                if goal.num == 0:       #どちらのゴール化を判定
                    text = font_score.render(str(goal.score), True, (0, 200, 255))
                    screan.disp.blit(text, [1400, 20])
                    goal0_score = goal.score

            text = font_time.render(f"{str(int(time))}s", True, (255, 255, 255))      #描画する経過時間の設定
            screan.disp.blit(text, [700, 20])                                         #経過時間の描画

            #ボールの増加を行う
            if int(time) % 10 == 0 and int(time) not in ball_num:
                ball_group.add(Ball(500, 450, -1, 1, 40, (0, 255, 0), sounds))        #ボール用コンテナにボールを追加
                #コンテナに追加した時点の時間を追加し、同時刻での二つ以上の追加を防ぐ
                ball_num.append(int(time))                                            

            for event in pg.event.get():
                if event.type == pg.QUIT: return
                if event.type == pg.USEREVENT:
                    time -= 1
                    if time < 0:            #時間が0秒未満になった時
                        screan_num = 2      #場面転換

        if screan_num == 2:         #screan_numが2になった時
            pg.display.update()
            screan.disp.fill((0,0,0))

            #得点の表示
            if goal1_score > goal0_score:
                screan.disp.blit(font_text_one.render("RED win", True, (255, 0, 0)), [100, 450])
                screan.disp.blit(font_text_one.render(f"{goal1_score} : {goal0_score}", True, (255, 255, 255)), [100, 100])
            elif goal1_score < goal0_score:
                screan.disp.blit(font_text_one.render("BLUE win", True, (0, 200, 255)), [100, 450])
                screan.disp.blit(font_text_one.render(f"{goal1_score} : {goal0_score}", True, (255, 255, 255)), [100, 100])
            else:
                screan.disp.blit(font_text_one.render("Drew", True, (0, 255, 0)), [100, 450])
                screan.disp.blit(font_text_one.render(f"{goal1_score} : {goal0_score}", True, (255, 255, 255)), [100, 100])

            for event in pg.event.get():
                if event.type == pg.QUIT: return

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


## 第5回
### Pygameでゲーム実装
#### 3限：基本機能
- ゲーム概要：
    - rensyu05/dodge_bomb.pyを実行すると，1600x900のスクリーンに草原が描画され，こうかとんを移動させ飛び回る爆弾から逃げるゲーム
    - こうかとんが爆弾と接触するとゲームオーバーで終了する
- 操作方法：矢印キーでこうかとんを上下左右に移動する
- プログラムの説明:
    - dodge_bomb.pyをコマンドラインから実行すると，pygameの初期化，main関数の順に処理が進む
    - Spriteクラスのcollide_rectにより，こうかとんと爆弾の接触を判定する
    - ゲームオーバーによりwhile文が停止する
    - main関数では，スクリーンの生成，背景画像の描画，こうかとんのコンテナ，爆弾のコンテナの作成を行う
    - main関数の無限ループではこうかとんの描画、爆弾描写、時間描写

#### 4限:追加機能
- プログラムの説明
    - 効果音機能：ボールが壁にあたった時に音がなる
    - timerクラス：プログラムの実行が始まってからの時間を表示するためのクラス

#### TODO
- 歩いているときの効果音の追加
- 背景が時間で変わる機能
- 爆弾のあたった時のこうかとんの画像変化

#### メモ
from itertools import count
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
        # rate：拡大率 
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
        self.image = pg.Surface((20, 20))                       #surfaceを用意
        pg.draw.circle(self.image , color, (10, 10), hankei)    #surfaceに円を描画
        self.rect = self.image.get_rect()                       #rect取得
        self.image.set_colorkey((0,0,0))
        self.rect.centerx =   random.randint(0, screen.rect.width)           #爆弾のｘ座標（ランダム）
        self.rect.centery =   random.randint(0, screen.rect.height)          #爆弾のｙ座標（ランダム）
        self.vx = speed_x
        self.vy = speed_y

    def update(self):
        self.rect.move_ip(self.vx, self.vy)

        if self.rect.centerx < 0 or self.rect.centerx > 1580:
            self.vx *= -1           #ボールの進む向き反転
            sounds[0].play()
        if self.rect.centery < 0 or self.rect.centery > 880:
            self.vy *= -1           #ボールの進む向き反転
            sounds[0].play()


class Timer:            #Timerクラス（時間を表示すする）
    def __init__(self, font, num):
        # font : 時間のフォント, num : 時間の初期値
        self.font = font
        self.counter = num
        self.text = self.font.render(str(self.counter), True, (155, 126, 255), (0,0,0))
        self.text.set_colorkey((0, 0, 0))

    def update(self):
        self.counter += 1       #一秒たす
        self.text = self.font.render(str(self.counter), True, (155, 126, 255), (0,0,0))
        self.text.set_colorkey((0, 0, 0))

def main():
    sounds[1].play()
    screan = Screan()       #コンストラクタを呼び出す
    timer = Timer(pg.font.Font("/Windows/Fonts/meiryo.ttc", 100) , 0)

    bombs = pg.sprite.Group()                                   #爆弾用のからのコンテナ作成
    for _ in range(5):
        bombs.add( Bomb((255, 0, 0), 10, 1, 1, screan) )        #爆弾を追加（五回）

    birds = pg.sprite.Group()                                   #こうかとん用のからのコンテナ作成
    birds.add(Bird("fig/6.png", 2, 900, 400))                   #こうかとんを追加

    pg.time.set_timer(pg.USEREVENT, 1000)

    while True:
        pg.display.update()
        screan.disp.blit(screan.image, (0,0))       #背景画像の貼り付け (0, 0)
  
        birds.update()                               #とり座標のアップデート
        birds.draw(screan.disp)                      #とり画像の貼り付け
 
        bombs.update()                               #爆弾座標のアップデート
        bombs.draw(screan.disp)                      #爆弾画像の貼り付け   

        screan.disp.blit(timer.text, (60,60))            

        if len(pg.sprite.groupcollide(birds, bombs, False, False)) != 0:        #とりが爆弾に衝突したとき
            return                                  #whileを抜ける

        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type == pg.USEREVENT:            #ユーザーイベントが起こった時
                timer.update()                        #タイマーのアップデートを行う
if __name__ == "__main__":
    pg.init()

    sounds = []                                       #BGM、効果音のリスト
    sounds.append(pg.mixer.Sound("oto/ball.wav"))     #効果音追加
    sounds.append(pg.mixer.Sound("oto/bgm.wav"))      #BGMの追加

    main()
    pg.quit()
    sys.exit()


## 第4回
### Pygameでゲーム実装
#### 3限：基本機能
- ゲーム概要：
    - rensyu04/dodge_bomb.pyを実行すると，1600x900のスクリーンに草原が描画され，こうかとんを移動させ飛び回る爆弾から逃げるゲーム
    - 爆弾は10秒ごとに増加する
    - こうかとんが爆弾と接触するとゲームオーバーで終了する
- 操作方法：矢印キーでこうかとんを上下左右に移動する
- プログラムの説明:
    - dodge_bomb.pyをコマンドラインから実行すると，pygameの初期化，main関数の順に処理が進む
    - Rectクラスのcolliderectメソッドにより，こうかとんと爆弾の接触を判定する
    - ゲームオーバーによりbakudan_proc関数,main_proc関数が停止する
    - main関数では，スクリーンの生成，背景画像の描画，こうかとんの描画，爆弾の描画を行う

    - main関数の無限ループでは時間の増加,bakudan_place関数の呼び出し
    - check_bound関数では，こうかとんや爆弾の座標がスクリーン外にならないようにチェックする
    - main_proc関数：こうかとん押された矢印キーの方向に移動するための関数

#### 4限:追加機能
- プログラムの説明
    - timer関数：プログラムの実行が始まってからの時間を表示するための関数
    - game_over関数：こうかとんが爆弾に触れたときに"GAME OVER"を表示する
    - bakudan_place関数：爆弾の初期位置をリストに追加するための関数
    - bakudan関数：爆弾を描写する
    - bakudan_proc関数：爆弾の位置を保存しているリストを更新し爆弾を動かすための関数
    - 爆弾はtimer関数を使って10秒ごとに一つ増える

#### TODO
- 爆弾に触れたときに画像が変わる機能
- 背景が時間で変わる機能

#### メモ
import pygame as pg
import sys
import random

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
            if counter not in num_list and counter % 10 == 0 and len(num_list)<=10:    #counterを１０で割った余りが０で
                num_list.append(counter)
                bakudan_place(random.randint(1, 1599), random.randint(1, 899))
            if r == True:
                run = False

#こうかとんを移動させる関数
def main_proc():
    global cx, cy
    if r == True:         #rがTrueになった時
        return            #関数を停止する

    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        cy -= 1
    elif key[pg.K_DOWN]:
        cy += 1
    elif key[pg.K_LEFT]:
        cx -= 1
    elif key[pg.K_RIGHT]:
        cx += 1

#爆弾の初期位置をリストに追加する関数
def bakudan_place(x, y):
    global num
    while True:
        if b_list[num] == False and num <= 10:          #b_list[num]がFalseでnumが１０以下の時
            b_list[num] = True                          #b_list[num]をTrueにする
            bx_list[num] = x                            #bx_list[num]に関数の引数ｘにする
            by_list[num] = y                            #by_list[num]に関数の引数ｙにする
            break

        num += 1

#爆弾を描画するための関数
def bakudan():
    global image_rect, r
    n = 0
    for i in b_list:
        if i == True:
            size = (20, 20)
            image = pg.Surface(size)                                 #２０ｘ２０のsurfaceを作成
            pg.draw.circle(image, (255,0,0), (10, 10), 10)           #surfaceの上に赤い円を作成
            image_rect = image.get_rect()
            image.set_colorkey((0,0,0))
            image_rect.center = bx_list[n], by_list[n]
            screan.blit(image, image_rect)

            r = tori_rect.colliderect(image_rect)                    #tori_rectとimage_rectが接触したときｒをTrueにする     
            n += 1
        else:
            break
    bakudan_proc()

#爆弾を移動させるための関数
def bakudan_proc():
    global bx_list, by_list, vx_list, vy_list
    if r == True:
        return

    m = 0
    for j in b_list:
        if j == True:
            bx_list[m] += vx_list[m]          #bx_list[m]にvx_list[m]を足す
            by_list[m] += vy_list[m]          #by_list[m]にvy_list[m]を足す
            m += 1
        else:
            break
    check_bound()

#こうかとんと爆弾が画面買いに出ないようにするための関数
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
                vx_list[q] *= -1                            #vx_list[q]の符号を反転する
            if by_list[q] < 0 or by_list[q] > 880:
                vy_list[q] *= -1                            #vy_list[q]の符号を反転する
            q += 1
        else:
            break

#時間を描画するための関数
def timer():
    font = pg.font.Font("/Windows/Fonts/meiryo.ttc", 100)                    #フォントと文字の大きさを設定する
    text = font.render(str(counter), True, (155, 126, 255), (0,0,0))
    text.set_colorkey((0, 0, 0))
    screan.blit(text, (60,60))

#爆弾に当たったときの処理をする関数
def game_over():
    if r == True:
        font = pg.font.Font("/Windows/Fonts/meiryo.ttc", 200)
        text = font.render("GAME OVER", True, (255, 55, 0), (0,0,0))
        text.set_colorkey((0, 0, 0))
        screan.blit(text, (200,250))
    

if  __name__ == "__main__":
    cx, cy = 900, 400
    counter = 0
    num = 0
    run = True
    num_list = []
    b_list = [False] * 10           #以下のリストに値が追加されてるかを判断するためのリスト
    bx_list = [0] * 10              #爆弾のx座標を保持するリスト
    by_list = [0] * 10              #爆弾のy座標を保持するリスト
    vx_list = [1] * 10              #こうかとんのx軸方向の符号を保持するリスト
    vy_list = [1] * 10              #こうかとんのｙ軸方向の符号を保持するリスト
    r = False

    pg.init()

    pg.display.set_caption("逃げろ！こうかとん")
    screan = pg.display.set_mode((1600, 900))
    
    main()

    pg.quit()
    sys.exit()


## 第3回
### tkinterで迷路ゲーム実装
#### 3限：基本機能
- ゲーム概要：
    - rensyu03/maze.pyを実行すると，1500x900のcanvasに迷路が描画され，迷路に沿ってこうかとんを移動させるゲーム
    - 実行するたびに迷路の構造は変化する
- 操作方法：矢印キーでこうかとんを上下左右に移動する
- プログラムの説明:
    - maze_makerモジュールのshow_maze関数でcanvasに迷路を描画する
    - PhotoImageクラスのコンストラクタとcreate_imageメソッドでこうかとんの画像を(1,1)に描画する
    - bindメソッドでKeyPressにkey_down関数を，KeyReleaseにkey_up関数を紐づける
    - main_proc関数で矢印キーに応じて，こうかとんを上下左右に1マス移動させ，afterメソッドで0.1秒後にmain_procを呼び出す
#### 4限:追加機能
- プログラムの説明
    - change_image関数：プログラム実行中に0~9のいずれかのボタンを押すことでこうかとんの画像を変更可能にする関数
    - 壁判定の追加：壁にこうかとんがめり込まないようにした
    - eval_fin 関数：ゴールテレビはないしたときに常時起動を停止し、こうかとんが停止するための関数
    - count_up 関数：プログラムの実行が始まった時からカウントアップを始めるための関数
    - create_enemy関数：敵キャラを画面中央に表示する
    - enemy_proc関数：敵キャラを移動させる
    - shi()関数：敵キャラに当たった時の反応（作り途中）
#### TODOs
- [shi()]敵キャラの当たり判定(あたると停止)
- [paint()]通過した床色を変化させる


import tkinter as tk
import maze_maker
import random
import tkinter.messagebox as tkm

def create_koukaton(x):                                                    
    global cx, cy, tori, tori_id, tori_num, tori
    tori_num = f"fig/{x}.png"
    tori = tk.PhotoImage(file=tori_num)
    tori_id = canvas.create_image(cx, cy, image = tori, tag = "tori")

def key_down(event):                                                           
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my, key
    if key == "Right" and meiro_list[my][mx+1] == 0:
        mx += 1
        cx += 100
    elif key == "Left" and meiro_list[my][mx-1] == 0:
        mx -= 1
        cx -= 100
    elif key == "Down" and meiro_list[my+1][mx] == 0:
        my += 1
        cy += 100
    elif key == "Up" and meiro_list[my-1][mx] == 0:
        my -= 1
        cy -= 100

    canvas.coords("tori", cx, cy)
    eval_fin()

def eval_fin():
    id = root.after(80, main_proc)
    if mx == goal_x and my == goal_y:
        root.after_cancel(id)                           #main_procの常時起動を停止
        root.after_cancel(time_id)                      #count_upの常時起動の停止
        tkm.showinfo("ゴール","おめでとうございます")

def count_up():
    global tmr, time_id
    tmr += 1
    entry.delete(0, tk.END)
    entry.insert(tk.END, tmr)
    time_id = root.after(1000, count_up)

def change_img():
    global tori_id, tori_num, tori
    key_list = ["0","1","2","3","4","5","6","7","8","9"]
    if key in key_list:
        canvas.delete(tori_id)                                  #起動時に描画したこうかとんの削除
        create_koukaton(key)                                    #押された番号のこうかとんを描画
    root.after(80, change_img)

def add_startgoal():
    global start_x, start_y, goal_x, goal_y, cx, cy, mx, my
    while True:
        start_x = random.randint(1, 4)
        start_y = random.randint(1, 8)
        goal_x = random.randint(10, 14)
        goal_y = random.randint(1, 8)
        if meiro_list[start_y][start_x] == 0 and meiro_list[goal_y][goal_x] == 0:
            break
    canvas.create_rectangle(start_x*100, start_y*100,                                       #スタート位置のマスを青くする
    start_x*100+100, start_y*100+100, fill="blue")
    canvas.create_rectangle(goal_x*100, goal_y*100,                                         #ゴール位置のマスを赤くする
    goal_x*100+100, goal_y*100+100, fill="red")
    cx = start_x*100+50
    cy = start_y*100+50
    mx = start_x
    my = start_y
                                            
def create_enemy():
    global enemy
    enemy = tk.PhotoImage(file="fig/1.png")
    teki_id = canvas.create_image(ex, ey, image = enemy, tag = "teki")
    enemy_proc()

def enemy_proc():
    global ex, ey, mex, mey, ey_num, mey_num
    print(mey)
    if mey == 0:
        ey_num*= -1
        mey_num*= -1
    elif mey == 8:
        ey_num *= -1
        mey_num*= -1
    ey += ey_num
    mey += mey_num

    canvas.coords("teki", ex, ey)
    enemy_id = root.after(1000, enemy_proc)

def shi():     #作り途中（enemyの当たり判定）
    global mx, my, mex, mey
    print(mey)
    print(my)
    if mex == mx and mey == my:
        root.after_cancel(id)                          
        root.after_cancel(time_id) 
        root.after(50, shi)


if __name__ == "__main__":
    mx = 1
    my = 1
    ex = 750
    ey = 50
    mex = 7
    mey = 0
    key = ""
    tmr = 0
    ey_num = -100
    mey_num = -1

    root = tk.Tk()
    root.geometry("1500x900")

    canvas = tk.Canvas(root, width=1500, height=900, background="black")
    canvas.place(x=0, y=0)

    entry = tk.Entry(justify = tk.CENTER,width=3,font=("Times New Roman", 43),background="green")   #タイマーを描画
    entry.grid(column = 0, row = 0, padx=5, pady=10)
    count_up()

    meiro_list = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, meiro_list)
    print(meiro_list)

    add_startgoal()
    create_koukaton(0)
    create_enemy()
    shi()

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    change_img()
    root.mainloop()


## 第2回
### tkinterで電卓実装
#### 追加機能
- クリアボタン：entryに入力されている数字を一文字づつ削除
- オールクリアボタン：entryに入力されている数字，数式の文字列全体をdeleteする
- 平方根ボタン: entryに入力されている数字を平方根へ変更
- sinボタン：entryに入力されている数字（角度）をsinに変換
- cosボタン：entryに入力されている数字（角度）をcosに変換
- tanボタン：entryに入力されている数字（角度）をtanに変換
- プラスマイナスボタン：entryに入力されている数字の符号を逆転
- ＋ボタン：entryに+を出力
- ーボタン：entryに-を出力
- ＊ボタン：entryに*を出力
- /ボタン：entryに/を出力

import tkinter as tk
import tkinter.messagebox as tkm
from turtle import back
from winreg import DeleteKey
import math

root = tk.Tk()
root.title("tk")
root.geometry("300x450")

k = 0
l = 1
n = 3
num_list = [7,8,9,4,5,6,1,2,3,".",0,"00"]
kigou_list = ["/","*", "-", "+"]
sannkaku = ["sin", "cos", "tan"]

entry = tk.Entry(justify = tk.RIGHT,width=10,font=("Times New Roman", 43))
entry.grid(column = 0, row = 0, padx=2, pady=2, columnspan=100)

def button__click(event):
    txt = event.widget["text"]
    entry.insert(tk.END, txt)

def get_Entry(event):
    s = entry.get()
    ans = eval(s)
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

def delete_Entry(event):
    entry.delete(0, tk.END)

def minus(event):
    num = entry.get()
    num_kai = -1 * int(num)
    entry.delete(0, tk.END)
    entry.insert(tk.END, num_kai)

def ruto(event):
    num = entry.get()
    num_kai = math.sqrt(int(num))
    entry.delete(0, tk.END)
    entry.insert(tk.END, num_kai)

def sannkaku_keisann(event):
    num = entry.get()
    txt = event.widget["text"]
    if txt == "sin":
        num = math.sin(math.radians(int(num)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, num)
    elif txt == "cos":
        num = math.cos(math.radians(int(num)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, num)
    elif txt == "tan":
        num = math.tan(math.radians(int(num)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, num)

def hitomoji_delete(event):
    pos_end_prev = len(entry.get())-1
    entry.delete(pos_end_prev,tk.END)


for i in num_list:
    button = tk.Button(root, text = i ,font = ("Times New Roman", 10),width=6, height = 4,background="aquamarine")
    button.grid(column = k%3, row = k//3+2, padx=4, pady=2)
    button.bind("<1>",button__click)
    k += 1

for j in kigou_list:
    button = tk.Button(root, text = j ,font = ("Times New Roman", 10),width=6, height = 4,background="gray")
    button.grid(column = 3, row = l, padx=4, pady=2)
    button.bind("<1>",button__click)
    l += 1

for t in sannkaku:
    button = tk.Button(root, text = t ,font = ("Times New Roman", 10),width=6, height = 4,background="gray")
    button.grid(column = 4, row = n, padx=4, pady=2)
    button.bind("<1>",sannkaku_keisann)
    n += 1

button1 = tk.Button(root, text = "=" ,font = ("Times New Roman", 10),width=6, height = 4, background="sky blue")
button1.grid(column = 3, row = 5, padx=4, pady=2)
button1.bind("<1>", get_Entry)

button2 = tk.Button(root, text = "C" ,font = ("Times New Roman", 10),width=6, height = 4, background="hot pink", fg = "red")
button2.grid(column = 0, row = 1, padx=4, pady=2)
button2.bind("<1>", delete_Entry)

button3 = tk.Button(root, text = "DEL" ,font = ("Times New Roman", 10),width=6, height = 4, background="hot pink")
button3.grid(column = 1, row = 1, padx=4, pady=2)
button3.bind("<1>", hitomoji_delete)

button4 = tk.Button(root, text = "+/-" ,font = ("Times New Roman", 10),width=6, height = 4, background="gray")
button4.grid(column = 2, row = 1, padx=4, pady=2)
button4.bind("<1>", minus)

