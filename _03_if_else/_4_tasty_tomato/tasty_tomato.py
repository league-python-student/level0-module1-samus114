from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
color = simpledialog.askstring('', 'red green or blue tomato?')

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if color == 'red':
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
elif color == 'green':
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="")
elif color == 'blue':
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")

canvas.create_rectangle(325, 100, 385, 230, fill="yellow", outline="")

root.mainloop()
