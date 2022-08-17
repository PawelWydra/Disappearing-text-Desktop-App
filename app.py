from tkinter import *
import tkinter.font as tkFont


# ---------------------------- BUTTONS FUNCTION ------------------------------- #

def five_sec():
    window.destroy()
    import time5


def ten_sec():
    window.destroy()
    import time10


# ---------------------------- CONSTANTS ------------------------------- #
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
GLabel_624.place(x=20, width=560, height=110)

GButton_395 = Button(window, command=five_sec)
GButton_395["anchor"] = "center"
GButton_395["bg"] = "#f0f0f0"
btn_ft = tkFont.Font(family='Times', size=18)
GButton_395["font"] = btn_ft
GButton_395["fg"] = "#000000"
GButton_395["justify"] = "center"
GButton_395["text"] = "5 sec"
GButton_395["bd"] = 0

GButton_395.place(x=100, y=400, width=120, height=50)

GButton_302 = Button(window, command=ten_sec)
GButton_302["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times', size=18)
GButton_302["font"] = ft
GButton_302["fg"] = "#000000"
GButton_302["justify"] = "center"
GButton_302["text"] = "10 sec"
GButton_302["bd"] = 0
GButton_302.place(x=380, y=400, width=120, height=50)

GLabel_329 = Label(window)
btn_ft = tkFont.Font(family='Times', size=23)
GLabel_329["font"] = btn_ft
GLabel_329["fg"] = "#333333"
GLabel_329["justify"] = "center"
GLabel_329["text"] = "Choose time to start text disappear"
GLabel_329.place(x=80, y=220, width=445, height=115)

window.mainloop()
