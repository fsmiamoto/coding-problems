from math import ceil

voltas, placas = [int(x) for x in input().split(' ')]

totalPlacas = voltas * placas

for i in range(1, 10):
    placa = ceil((i / 10) * totalPlacas)
    print('{}'.format(placa), end='')
    if i < 9:
        print(' ', end='')
    else:
        print()
