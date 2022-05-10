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