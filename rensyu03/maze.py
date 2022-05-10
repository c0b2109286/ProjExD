from email.mime import image
import tkinter as tk
import maze_maker

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
    root.after(80, main_proc)

if __name__ == "__main__":
    mx = 1
    my = 1
    cx = 150
    cy = 150
    key = ""
    root = tk.Tk()
    root.geometry("1500x900")
    canvas = tk.Canvas(root, width=1500, height=900, background="black")
    canvas.place(x=0, y=0)
    meiro_list = maze_maker.make_maze(15, 9)
    print(meiro_list)
    maze_maker.show_maze(canvas, meiro_list)
    create_koukaton()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(80, main_proc)
    root.mainloop()