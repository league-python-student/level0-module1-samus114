from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    dob = "password"
    scrtmsg = simpledialog.askstring(None, "what is the message of secretness")
    guess = simpledialog.askstring(None, "what is the password of the secret message?")
    if guess == dob:
        messagebox.showinfo(None, scrtmsg)
    else:
        messagebox.showerror(None, "INTRUDER")