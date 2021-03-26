from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    dob = simpledialog.askstring(None, "Please enter your date of birth (month/dd)")
    if dob.lower() == "march 26":
        messagebox.showinfo(None, "Happy Birthday to You!")
    else:
        messagebox.showinfo(None, "happy UNBIRTHDAY HAHAHAH")