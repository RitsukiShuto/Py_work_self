# Created by RitsukiShuto on 2020/03/15.
# Python TextBook Chapter2-5 "BMI.py"
#
# 体重と身長を入力
weight = float(input("体重を入力してください(kg):"))
length = float(input("身長を入力してください(m):"))
# BMIを計算
BMI = weight / (length * length)
# ステータスを判定
if BMI < 18.5:
    state = "やせ型"
elif BMI >= 18.5 and BMI <= 25.0:
    state = "普通"
elif BMI >= 25.0 and BMI <= 30.0:
    state = "肥満(軽度)"
else:
    state = "肥満(重度)"
# 結果を出力
print("あなたのBMI値は,{0}で{1}です。".format(BMI, state))