# Created by RitsukiShuto on 2020/03/12.
# Python TextBook chapter 2-3 "inch-to-cm.py", "format-key.py"
#
# インチをセンチに変換
PER_INCH = 2.54
inch = 24
cm = PER_INCH * inch
# 文字列を作成
desc = "{0}インチ = {1}センチ".format(inch, cm)
print(desc)
print("------------------------")

# (1)
print("私は{name}です。".format(name="オカモト"))

# (2)
fmt = "年齢は{age}歳で, 職業は{job}です。"
s = fmt.format(age=22, job="プログラマ")
print(s)
