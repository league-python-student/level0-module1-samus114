"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = tk.Tk()
    window.withdraw()
    num1 = simpledialog.askinteger('', 'what is the first number you would like to use?')
    num2 = simpledialog.askinteger('', 'what is the secnd number to be used?')
    operation = simpledialog.askstring('', 'would you like to add, subtract, multiply, or divide?')
    if operation == 'add':
        messagebox.showinfo('add', 'your final numbers were: ' + str(num1) + ' and ' + str(num2) + ' which equals ' + str(num1 + num2))
    if operation == 'subtract':
        messagebox.showinfo('subtract', 'your final numbers were: ' + str(num1) + ' and ' + str(num2) + ' which equals ' + str(num1 - num2))
    if operation == 'multiply':
        messagebox.showinfo('multiply', 'your final numbers were: ' + str(num1) + ' and ' + str(num2) + ' which equals ' + str(num1 * num2))
    if operation == 'divide':
        messagebox.showinfo('divide', 'your final numbers were: ' + str(num1) + ' and ' + str(num2) + ' which equals ' + str(num1 / num2))