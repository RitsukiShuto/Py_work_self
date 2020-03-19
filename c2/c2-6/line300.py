# Created by RitsukiShuto on 2020/03/18.
# Python TextBook Chaoter 2-6 "tetesen.py"
#
# グラフィックスライブラリを読み込み
from tkinter import *
# 画面の初期化
w = Canvas(Tk(), width=900, height=400)
w.pack()

# 線を引く
for i in range(300):
    x = i * 3
    #            (x1,y1,x2,y2,  fill="color")
    w.create_line(x, 0, x, 400, fill="#000000")

mainloop()
