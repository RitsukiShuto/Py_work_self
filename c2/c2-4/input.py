# Created by RitsukiDhuto on 2020/03/13.
# Python TextBook Chapter 2-4 "hello-input.py", "inch-to-cm-input.py"
#
# 名前を入力
name = input("お名前は:")
# 結果を出力
print(name + "さん、こんにちは。")
print("-------------------------")

# インチをセンチに変換
PER_INCH = 2.54
# 値を入力
inch = input("何インチですか？：")
# 値を計算
cm = PER_INCH * int(inch)
# 結果を出力
print("{0}インチは{1}センチです。".format(str(inch), str(cm)))
