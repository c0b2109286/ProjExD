from email.mime import image
import tkinter as tk

def create_koukaton():
    global cx, cy, tori
    cx = 300
    cy = 400
    tori = tk.PhotoImage(file="fig/5.png")
    canvas.create_image(cx, cy, image = tori, tag = "tori")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x900")
    canvas = tk.Canvas(root, width=1500, height=900, background="black")
    canvas.place(x=0, y=0)
    create_koukaton()
    root.mainloop()