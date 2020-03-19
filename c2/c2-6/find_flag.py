# Created by Ritsuki Shuto on 2020/03/19.
# Python TextBook Chapter 2-6 "find-flag.py"
#
# for文をフラグ分岐する場合
# データを作成
foodstuff = ["Banana", "Mango", "Fish", "Carrot", "Cabbage"]

# マンゴーを検索
flag_find = False
for food in foodstuff:
    if food == "Mango":
        flag_find = True
        break

if flag_find:
    print("マンゴーが入っています。")
else:
    print("ありません。")

