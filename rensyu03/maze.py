from email.mime import image
import tkinter as tk

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

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x900")
    canvas = tk.Canvas(root, width=1500, height=900, background="black")
    canvas.place(x=0, y=0)
    create_koukaton()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_down)
    root.mainloop()