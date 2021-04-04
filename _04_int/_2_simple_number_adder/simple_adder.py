"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = tk.Tk()
    window.withdraw()
    num1 = simpledialog.askinteger('', 'what is your first number to be added?')
    num2 = simpledialog.askinteger('', 'what is the second number to be added?')
    messagebox.showinfo('', 'your number is ' + str(num1+num2))
    window.mainloop()