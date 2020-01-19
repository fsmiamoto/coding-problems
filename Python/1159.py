while True:
    n = int(input())

    if n == 0:
        break

    if n % 2 != 0:
        n += 1

    sum = 0
    next = n

    for _ in range(5):
        sum += next
        next += 2

    print(sum)
