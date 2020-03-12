# Created by RitsukiShuto on 2020/03/12.
# Python TextBook chapter 2-3 "str-num.py", "renketu.py", "inch-to-cm2.py"
#
# 数値と文字列を連結
get_temp = 30
temp = str(get_temp)
print("今日の気温は" + temp + "℃です。")
print("--------------------------------")

# 名前と年齢を連結
name = "okamoto"
age = "19"
# 文字列を連結
desc = name + "は今年で" + str(age) + "歳です。"
print(desc)
print("--------------------------------")

# インチをセンチに変換
PER_INCH = 2.54
inch = 24
cm = PER_INCH * inch
# 文字列を作成
desc = str(inch) + "インチ=" + str(cm) + "センチ"
print(desc)
