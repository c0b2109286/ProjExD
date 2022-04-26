import tkinter as tk

root = tk.Tk()
root.title("tk")
root.geometry("300x450")

(x, y) = (0, 0)
num_list = [9, 6, 3, 8, 5, 2, 7, 4, 1]
def button_one(num, x, y):
    button = tk.Button(root, text = num ,font = ("Times New Roman", 30))
    button.grid(column = x, row = y)

for i in num_list:
    button_one(i, x, y)
    if y == 2:
        x += 1
        y = 0
    else:
        y += 1

button_one(0, 0, 4)
root.mainloop()