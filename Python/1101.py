while True:
    a, b = (int(x) for x in input().split())
    # End signal
    if a <= 0 or b <= 0:
        break

    # a will be less than b
    a, b = (a, b) if b > a else (b, a)

    values = list(range(a, b + 1))
    [ print(x, end=' ') for x in values ]
    print('Sum={}'.format(sum(values)))