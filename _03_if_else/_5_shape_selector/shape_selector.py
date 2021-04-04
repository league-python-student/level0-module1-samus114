import turtle
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    root = tk.Tk()
    canvas = tk.Canvas(root, width=600, height=600, bg="#DDDDDD")
    canvas.grid()
    # Make a new turtle
    tur = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring('', 'what shape should I draw?')
    # Draw the shape requested by the user using if-elif-else statements
    if shape == 'oval':
        canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    elif shape == 'circle':
        canvas.create_oval(200, 200, 300, 300, fill="red", outline="")
    elif shape == 'square':
        canvas.create_rectangle(200, 200, 300, 300, fill="red", outline="")
    # Call the turtle .done() method
    turtle.done()
    root.mainloop()