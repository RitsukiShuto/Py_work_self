# Created by RitsukiShuto on 2020/03/16.
# Python TextBook Chapter 2-5 "leapyear.py"
#
# 西暦を入力
year = int(input("西暦を入力:"))
# 結果を格納
leap_res = False
# うるう年か判定
if year % 4 == 0 and year % 100 != 0:
    leap_res = True
elif year % 400 == 0:
    leap_res = True
else:
    pass
# 結果を出力
if leap_res:
    res = "です"
else:
    res = "ではありません"
print("{0}年はうるう年{1}。".format(year, res))
