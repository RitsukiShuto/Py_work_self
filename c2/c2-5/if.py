# Created by RitsukiShuto on 2020/03/15.
# Python TextBook Chapter2-5 "if-cafe.py", "even-odd.py", "if-noelse.py"
#
# 条件文岐
temp = 26
if temp >= 25:
    print("氷を出す。")
else:
    print("水を出す。")
# 奇数、偶数判定
num = int(input("整数を入力:"))
if num % 2 == 0:
    print("偶数です。")
else:
    print("奇数です。")
# else文がないif文
level = 10
if level > 5:
    print("レベル5以上のアドバイス")
if level > 8:
    print("レベル8以上のアドバイス")