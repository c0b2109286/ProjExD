#　プロジェクト演習I・テーマD
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
#### 4限：追加機能
- プログラムの説明
    - change_image関数：プログラム実行中に0~9のいずれかのボタンを押すことでこうかとんの画像を変更可能にする関数
    - 壁判定の追加：壁にこうかとんがめり込まないようにした
    - eval_fin 関数：ゴールしたときに常時起動を停止し、こうかとんが停止するための関数
    - count_up 関数：プログラムの実行が始まった時からカウントアップを始めるための関数

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

