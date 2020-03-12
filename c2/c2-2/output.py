# Created by RitsukiShuto on 2020/03/10.
# Python TextBook Chapter 2-2 "kakugen.py", "nennrei.py", "print-end.py", "daikei.py"
#
# 格言を表示する
print("たたき続けなさい")
print("そうすれば開かれます")

print("------------------------------")
# 数値に説明を加えて表示
age = 18
print("年齢は、", age, "歳です。")

print("------------------------------")
# print()で改行しない方法
print("剣で突き刺すかのように", end="")
print("話すものがいる。", end="")
print("しかし賢い者たちの舌は", end="")
print("人を癒す。")

print("------------------------------")
# 台形の面積を求める
a = 2
b = 3
height = 4
s = (a + b) * height / 2
print("台形の面積は、", s, "[cm]")
