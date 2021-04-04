# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
import math
import tkinter as tk
from tkinter import simpledialog, messagebox

if __name__ == '__main__':
    root = tk.Tk()
    circle = simpledialog.askinteger('', 'what is the radius')
    which = simpledialog.askstring('', 'do you want to calculate area or circumference')
    if which == 'area':
        messagebox.showinfo('', str(math.pi + (circle*circle)) + ' is the area')
    elif which == 'circumference':
        messagebox.showinfo('', str(2*math.pi*circle) + 'is the circumference')
    root.mainloop()
