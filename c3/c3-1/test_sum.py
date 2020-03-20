# Created by Ritsuki Shuto on 2020/03/19.
# Python TextBook Chapter 3-1 "test-sum.py", "test-sum2.py"
#
# リストを作成
points = [88, 76, 67, 43, 79, 80, 91]
sum_v = 0

# 合計を求める
for i in points:
    sum_v += i
    print(i, "点足して合計:", sum_v)

# 平均を求める
avg = sum_v / len(points)
print("平均点:", avg)

# 合計を求める -2
sum_v = sum(points)
avg = sum_v / len(points)

print("合計:", sum_v)
print("平均:", avg)