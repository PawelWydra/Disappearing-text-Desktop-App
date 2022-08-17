from tkinter import *
import tkinter.font as tkFont


def count_down(count=10):
    global text, timer
    if text == GLabel_329.get(1.0, END):
        if count > 0:
            timer = window.after(1000, count_down, count - 1)
            count_sec = count % 60
            count_sec = f"You have {count_sec} second left"
            GLabel_633.config(text=count_sec)
        else:
            GLabel_633.config(text="Time over")
            GLabel_329.delete(1.0, END)
            GLabel_329.insert(END, "")
            timer = window.after(2000, count_down)
    else:
        text = GLabel_329.get(1.0, END)
        timer = window.after(1000, count_down)
        count_sec = count % 60
        count_sec = f"You have {count_sec} second left"
        GLabel_633.config(text=count_sec)


# ---------------------------- CONSTANTS ------------------------------- #

timer = None
time = 10
text = ""
YELLOW = "#f7f5dd"
window = Tk()
window.title("Disappearing Text Application")
window.config(padx=100, pady=50, bg=YELLOW)

# setting window size
width = 800
height = 600
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(alignstr)
window.resizable(width=False, height=False)

GLabel_624 = Label(window)
GLabel_624["anchor"] = "center"
ft = tkFont.Font(family='Times', size=34)
GLabel_624["font"] = ft
GLabel_624["fg"] = "#333333"
GLabel_624["justify"] = "center"
GLabel_624["text"] = "Disappearing Text Application"
GLabel_624.place(x=20, width=560, height=100)

GLabel_625 = Label(window)
GLabel_625["anchor"] = "center"
ft = tkFont.Font(family='Times', size=20)
GLabel_625["font"] = ft
GLabel_625["fg"] = "#333333"
GLabel_625["justify"] = "center"
GLabel_625["text"] = "Start typing :)"
GLabel_625.place(x=100, y=120, width=400, height=100)

GLabel_329 = Text(window)
GLabel_329["fg"] = "#333333"
ft = tkFont.Font(family='Times', size=20)
GLabel_329["font"] = ft
GLabel_329.place(x=80, y=220, width=445, height=100)

GLabel_633 = Label(window)
GLabel_633["anchor"] = "center"
ft = tkFont.Font(family='Times', size=14)
GLabel_633["font"] = ft
GLabel_633["fg"] = "#333333"
GLabel_633["justify"] = "center"
GLabel_633["text"] = f"Time remaining to text disappear {time}"
GLabel_633.place(x=150, y=360, width=300, height=100)

window.bind(count_down())

