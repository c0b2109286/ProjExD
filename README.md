# プロジェクト演習I・テーマD
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

