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
        # bx:ボールのｙ座標, by:ボールのx座標,vx:ボール（ｘ方向）進む速さ
        # vy:ボール（ｙ方向）に進む速さ,sounds:bgmのリスト
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
    #使用するフォント
    font_score, font_time = pg.font.Font(None, 150), pg.font.Font(None, 200)
    font_text_one, font_text_two = pg.font.Font(None, 350), pg.font.Font(None, 250)                                   
    ball_num = []       #ボールが追加された時間を保持するリストの初期化
    screan_num = 0      #スタート画面、プレイ画面、結果画面切り替え用numの初期化
    time = 60            #時間の初期化
    pg.time.set_timer(pg.USEREVENT, 1000)       #1秒ごとにUSEREVENTを実行
    #BGM、効果音のリスト
    sounds = [pg.mixer.Sound("oto/ball.wav"), pg.mixer.Sound("oto/bgm1.wav"), \
                pg.mixer.Sound("oto/goal1.wav"), pg.mixer.Sound("oto/goal2.wav"),  \
                    pg.mixer.Sound("oto/mallet.wav"), pg.mixer.Sound("oto/start.wav")]        

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
                        if ball.rect.centerx >= mallet.rect.centerx + 35 or \
                                    ball.rect.centerx <= mallet.rect.centerx - 35:
                            ball.vx *= -1
                            sounds[4].play()
                        if ball.rect.centery >= mallet.rect.centery + 35 or \
                                    ball.rect.centery <= mallet.rect.centery - 35:
                            ball.vy *= -1
                            sounds[4].play()

            #ゴールとボールの衝突判定と得点の増加を行う
            for goal in goals:                  #ゴール用のコンテナから一つずつ取り出す
                for ball in ball_group:         #ボール用のコンテナから一つずつ取り出す
                    if pg.sprite.collide_rect(goal, ball):
                        if ball.rect.centerx >= goal.rect.centerx + 5 or\
                                     ball.rect.centerx <= goal.rect.centerx - 5:
                            ball.vx *= -1
                            goal.score += 1         #得点を追加
                            if goal.num == 1: sounds[2].play()
                            else:sounds[3].play()
                                
                        if ball.rect.centery >= goal.rect.centery + 200 or \
                                    ball.rect.centery <= goal.rect.centery - 200:
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
                #ボール用コンテナにボールを追加
                ball_group.add(Ball(500, 450, -1, 1, 40, (0, 255, 0), sounds))        
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
            if goal1_score > goal0_score:       #左側が勝利の場合
                screan.disp.blit(font_text_one.render("RED win", True, (255, 0, 0)), [100, 450])
                txt = f"{goal1_score} : {goal0_score}"
                screan.disp.blit(font_text_one.render(txt, True, (255, 255, 255)), [100, 100])
            elif goal1_score < goal0_score:     #右側が勝利の場合
                screan.disp.blit(font_text_one.render("BLUE win", True, (0, 200, 255)), [100, 450])
                txt = f"{goal1_score} : {goal0_score}"
                screan.disp.blit(font_text_one.render(txt, True, (255, 255, 255)), [100, 100])
            else:                               #引き分けの場合
                screan.disp.blit(font_text_one.render("Drew", True, (0, 255, 0)), [100, 450])
                txt = f"{goal1_score} : {goal0_score}"
                screan.disp.blit(font_text_one.render(txt, True, (255, 255, 255)), [100, 100])

            for event in pg.event.get():
                if event.type == pg.QUIT: return

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()