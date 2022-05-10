import tkinter as tk

def canvas():
    global cx, cy, tori
    cx = 300
    cy = 400
    canvas = tk.Canvas(root, width=1500, height=900, background="black")
    canvas.place(x=0, y=0)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x900")
    canvas()
    root.mainloop()