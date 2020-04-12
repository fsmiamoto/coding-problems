import fileinput

for line in fileinput.input():
    h, m = [int(x) for x in line.split(':')]

    # Máximo atraso
    m += 60

    if m > 60:
        h += 1
        m -= 60

    if h >= 8:
        atraso = (h - 8) * 60 + m
        print('Atraso maximo: {}'.format(atraso))
    else:
        print('Atraso maximo: {}'.format(0))
