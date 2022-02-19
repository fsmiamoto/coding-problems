import sys

for line in sys.stdin:
    n = int(line)
    x, y = n // 3, n - n // 3 - 1

    for i in range(n):
        for j in range(n):
            if i == n // 2 and j == n // 2:
                print(4, end='')
            elif i >= x and i <= y and j >= x and j <= y:
                print(1, end='')
            elif i == j:
                print(2, end='')
            elif i + j == n - 1:
                print(3, end='')
            else:
                print(0, end='')
        print()

    print()
