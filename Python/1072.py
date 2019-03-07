n = int(input())

for _ in range(n):
    x = int(input())
    if x > 0: 
        if x % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    elif x < 0:
        if x % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
    else:
        print('NULL')
