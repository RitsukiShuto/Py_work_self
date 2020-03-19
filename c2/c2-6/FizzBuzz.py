# Created by Ritsuki Shuto on 2020/03/19.
# Python TextBook Chapter 2-6 "fizzbuzz.py"
#
for i in range(1, 21):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i, "FizzBuzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    elif i % 5 == 0:
        print(i, "Buzz")
    else:
        print(i)
