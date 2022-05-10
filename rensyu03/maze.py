from email.mime import image
import tkinter as tk
import maze_maker

cx = 300
cy = 400
key = ""

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
    global cx, cy, key
    if key == "Right":
        cx += 20
    elif key == "Left":
        cx -= 20
    elif key == "Down":
        cy += 20
    elif key == "Up":
        cy -= 20
    canvas.coords("tori", cx, cy)
    root.after(20, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x900")
    canvas = tk.Canvas(root, width=1500, height=900, background="black")
    canvas.place(x=0, y=0)
    meiro_list = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, meiro_list)
    create_koukaton()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(20, main_proc)
    root.mainloop()