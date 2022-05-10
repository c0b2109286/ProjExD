import tkinter as tk
import maze_maker
import random
import tkinter.messagebox as tkm

def create_koukaton():
    global cx, cy, tori
    tori = tk.PhotoImage(file="fig/5.png")
    canvas.create_image(cx, cy, image = tori, tag = "tori")

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
    create_koukaton()

def eval_fin():
    id = root.after(80, main_proc)
    if mx == goal_x and my == goal_y:
        root.after_cancel(id)
        #tkm.showinfo("ゴール","おめでとうございます")

def add_startgoal():
    global start_x, start_y, goal_x, goal_y, cx, cy, mx, my
    while True:
        start_x = random.randint(1, 14)
        start_y = random.randint(1, 8)
        goal_x = random.randint(1, 14)
        goal_y = random.randint(1, 8)
        if meiro_list[start_y][start_x] == 0 and meiro_list[goal_y][goal_x] == 0:
            break
    canvas.create_rectangle(start_x*100, start_y*100, start_x*100+100, start_y*100+100, fill="blue")
    canvas.create_rectangle(goal_x*100, goal_y*100, goal_x*100+100, goal_y*100+100, fill="red")
    cx = start_x*100+50
    cy = start_y*100+50
    mx = start_x
    my = start_y

if __name__ == "__main__":
    mx = 1
    my = 1
    key = ""

    root = tk.Tk()
    root.geometry("1500x900")

    canvas = tk.Canvas(root, width=1500, height=900, background="black")
    canvas.place(x=0, y=0)

    meiro_list = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, meiro_list)

    add_startgoal()
    create_koukaton()


    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()