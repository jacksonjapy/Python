"""
By Jackson Ja
"""
from tkinter import Tk, Label
from time import time, strftime


def update_time():
    label.config(text=strftime("%Y-%m-%d %H:%M:%S"))
    window.after(1000, update_time)


if __name__ == '__main__':
    window = Tk()
    window.title("系统时间")
    label = Label(window, font=("Arial", 36), bg="white", fg="black")
    label.pack(padx=10, pady=10)
    update_time()
    window.mainloop()
