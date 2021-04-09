import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = tk.Tk()
    window.withdraw()
    for x in range(0, 16):
        year = 2006+x
        messagebox.showinfo('', str(year))
window.mainloop()