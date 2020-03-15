# Created by RitsukiShuto on 2020/03/15.
# Python TextBook Chapter2-4 "ct-to-g.py", "jikyu.py"
#
# カラットをグラムに変換
PER_CT = 0.2
# ユーザが数値を入力
user = input("何カラットですか？:")
# 浮動小数点型に変換
ct = float(user)
# 計算
gram = PER_CT * ct
# 結果を出力
print("{0}カラットは{1}グラムです。".format(ct, gram))
print("--------------------------")

# 時給を計算
# 時給を入力
pph = int(input("時給はいくらですか？:"))    # pph => payment_per_hour
# 時間を入力
time = int(input("何時間働きましたか？:"))
# 計算
pay = pph * time
# 結果を出力
fmt = """
時給{0}円で、{1}時間働いたので
給料は{2}円です。
"""
desc = fmt.format(pph, time, pay)
print(desc)