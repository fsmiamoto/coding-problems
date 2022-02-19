# 1161.py

from math import factorial

while True:
    try:
        a, b = [int(x) for x in input().split()]
        print('{}'.format(factorial(a) + factorial(b)))
    except:
        break
