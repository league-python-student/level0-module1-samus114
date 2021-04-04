"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    root = tk.Tk()
    riddlecor = 0
    riddle1 = simpledialog.askstring('', 'How much will a 38° angle measure when looked at under a microscope that magnifies ten times?(write num like 2 200 or 21 no degree sign)')
    if riddle1 == '38':
        riddlecor += 1
    riddle2 = simpledialog.askstring('', 'Before Mount Everest was discovered, what was the highest mountain on Earth?')
    if riddle2 == 'mount everest':
        riddlecor += 1
    riddle3 = simpledialog.askstring('', 'The more you take, the more you leave behind. What am I?')
    if riddle2 == 'footsteps':
        riddlecor += 1
    messagebox.showinfo('', 'your score is: ' + str(riddlecor))
    root.mainloop()