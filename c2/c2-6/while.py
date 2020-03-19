# Created by RitsukiShuto on 2020/03/18.
# Python TextBook Chapter "while-simple.py", "tubo.py", "tubo2.py"
#
# 疑似的に車を走らせる
energy = 3
while energy > 0:
    print("+走る")
    print("|energy = ", energy)
    energy =- 1
print("----------")

# 繰り返し坪数を調べる
while True:
    tubo = int(input("調べる坪数は？:"))
    m2 = tubo * 3.31
    print("{0}坪は{1}平方メートルです。".format(tubo, m2))
print("----------")
# src => "tubo2.py"
while True:
    user = input("坪数は?:")
    if user == "" or user == "q": break
    tubo = int(user)
    m2 = user * 3.31
    print("{0}坪は{1}平方メートルです。".format(tubo, m2))
print("---------")