n = int(input())
if n % 2 == 0:
    n = n + 1
    for _ in range(6):
        print(n)
        n += 2
else:
    for _ in range(6):
        print(n)
        n = n + 2
