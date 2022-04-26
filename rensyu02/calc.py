import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("tk")
root.geometry("300x450")

(x, y) = (0, 0)
num_list = [9, 6, 3, 8, 5, 2, 7, 4, 1]

def button_one(num, x, y):
    button = tk.Button(root, text = num ,width=5, height = 5)
    button.grid(column = x, row = y, padx=10, pady=10)
    button.bind("<1>",button__click)

def button__click(event):
    txt = event.widget["text"]
    tkm.showinfo(txt, f"[{txt}]のボタンが押されました")

for i in num_list:
    button_one(i, x, y)
    if y == 2:
        x += 1
        y = 0
    else:
        y += 1

button_one(0, 0, 4)

root.mainloop()