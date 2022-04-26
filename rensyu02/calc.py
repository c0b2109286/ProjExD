import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("tk")
root.geometry("300x450")

k = 0
num_list = [7,8,9,4,5,6,1,2,3,0]

entry = tk.Entry(justify = tk.RIGHT,width=10,font=("Times New Roman", 40))
entry.grid(column = 0, row = 0, padx=10, pady=0, columnspan=100)

def button__click(event):
    txt = event.widget["text"]
    entry.insert(tk.END, txt)

def get_Entry(event):
    s = entry.get()
    ans = eval(s)
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

for i in num_list:
    button = tk.Button(root, text = i ,font = ("Times New Roman", 30))
    button.grid(column = k%3, row = k//3+2, padx=0, pady=10)
    button.bind("<1>",button__click)
    k += 1

button = tk.Button(root, text = "+" ,font = ("Times New Roman", 30))
button.grid(column = 3, row = 4, padx=0, pady=10)
button.bind("<1>",button__click)

button1 = tk.Button(root, text = "=" ,font = ("Times New Roman", 30))
button1.grid(column = 3, row = 5, padx=0, pady=10)

button1.bind("<1>", get_Entry)

root.mainloop()