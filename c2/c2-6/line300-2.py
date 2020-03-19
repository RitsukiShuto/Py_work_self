# Created by Ritsuki Shuto on 2020/03/19.
# Python TextBook Chapter 2-6 "tatesen2.py"
#
from tkinter import *

w = Canvas(Tk(), width=900, height=400)
w.pack()

# 線を交互に引く
for i in range(100):
    x = i * 9
    if i % 2 == 0:
        c = "#ff0000"

    else:
        c = "#0000FF"
    w.create_line(x, 0, x, 400, fill=c)

mainloop()
