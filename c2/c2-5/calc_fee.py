# Created by RitsukiShuto on 2020/03/15.
# Python TextBook Chapter2-5 "calc-fee.py"
#
# 遊園地の入場料を計算するプログラム
# 人数の入力
MemberOfChildren = int(input("子供料金の人数を入力:"))
MemberOfNormal = int(input("普通料金の人数を入力:"))
MemberOfElder = int(input("年配者料金の人数を入力"))
# 人数の合計
MemberOfPeople = MemberOfChildren + MemberOfNormal + MemberOfElder
# 料金の計算
CostOfChildren = 500 * MemberOfChildren     # 子供料金
CostOfNormal = 1000 * MemberOfNormal        # 普通料金
CostOfElder = 700 * MemberOfElder           # 年配者料金
CostOfTotal = CostOfChildren + CostOfNormal + CostOfElder  # 合計金額
# 団体割引の計算
if MemberOfPeople >= 10:
    print("団体割引があります。")
    CostOfTotal *= 0.8
else:
    print("団体割引はありません。")

# 結果を出力
print("合計金額 : {0}人, {1}円".format(MemberOfPeople, CostOfTotal))
print("子供　　料金 : {0}人 ×  500円 = {1}円".format(MemberOfChildren, CostOfChildren))
print("普通　　料金 : {0}人 × 1000円 = {1}円".format(MemberOfNormal, CostOfNormal))
print("年配者　料金 : {0}人 ×  700円 = {1}円".format(MemberOfElder, CostOfElder))
