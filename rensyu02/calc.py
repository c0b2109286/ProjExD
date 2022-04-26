import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("tk")
root.geometry("300x450")

k = 0
num_list = [7,8,9,4,5,6,1,2,3,0]

entry = tk.Entry(justify = tk.RIGHT,width=10,font=("Times New Roman", 40))
entry.grid(column = 0, row = 0, padx=10, pady=0, columnspan=10)

def button__click(event):
    txt = event.widget["text"]
    tkm.showinfo(txt, f"[{txt}]のボタンが押されました")

for i in num_list:
    button = tk.Button(root, text = i ,font = ("Times New Roman", 30))
    button.grid(column = k%3, row = k//3+2, padx=0, pady=10)
    button.bind("<1>",button__click)
    k += 1

root.mainloop()