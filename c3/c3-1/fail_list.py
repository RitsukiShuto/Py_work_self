# Created by RitsukiShuto on 2019/03/20.
# Python TextBook Chapter c3-1 "fail_list.py"
#
# 点数のリストを生成
points = [80, 40, 23, 14, 29, 58]

# 30点未満をリストに追加
Fail_List = []
for i in points:
    if i < 30:
        Fail_List.append(i)

# 赤点リストを表示
print(Fail_List)
