#Let's create a digital clock with python
#font_link: https://www.dafont.com/ds-digital.font

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("DS-Digital", 100), background="black", foreground="white")
label.pack(anchor='center')
time()

mainloop()