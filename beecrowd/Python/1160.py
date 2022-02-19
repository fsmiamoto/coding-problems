n = int(input())

for _ in range(n):
    popA, popB, crescA, crescB = [float(x) for x in input().split()]
    anos = 0

    taxaA = crescA / 100
    taxaB = crescB / 100

    popA = int(popA)
    popB = int(popB)

    while popA <= popB:
        crescA = int(popA * taxaA)
        popA += crescA

        crescB = int(popB * taxaB)
        popB += crescB

        anos += 1

        if anos > 100:
            break

    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(anos))
