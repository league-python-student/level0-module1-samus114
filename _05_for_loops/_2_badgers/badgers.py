import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = tk.Tk()
    window.withdraw()
    for x in range(0, 3):
        if x != 2:
            for x in range (0, 14):
                if x <= 11:
                    print('badger')
                else:
                    print('mushroom')
        else:
            print('a snake!!!')
window.mainloop()