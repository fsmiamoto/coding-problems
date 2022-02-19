firstCase = True
while True:
    n = int(input())

    if n == 0:
        break

    shirts = {
        'branco': {
            'P': [],
            'M': [],
            'G': [],
        },
        'vermelho': {
            'P': [],
            'M': [],
            'G': [],
        }
    }

    for i in range(n):
        name = input()
        color, size = input().split(' ')
        shirts[color][size].append(name)
        # bisect.insort(shirts[color][size], name)

    if firstCase:
        firstCase = False
    else:
        print()

    shirts['branco']['P'].sort()
    shirts['branco']['M'].sort()
    shirts['branco']['G'].sort()
    shirts['vermelho']['P'].sort()
    shirts['vermelho']['M'].sort()
    shirts['vermelho']['G'].sort()

    for nome in shirts['branco']['P']:
        print('branco P', nome)

    for nome in shirts['branco']['M']:
        print('branco M', nome)

    for nome in shirts['branco']['G']:
        print('branco G', nome)

    for nome in shirts['vermelho']['P']:
        print('vermelho P', nome)

    for nome in shirts['vermelho']['M']:
        print('vermelho M', nome)

    for nome in shirts['vermelho']['G']:
        print('vermelho G', nome)
