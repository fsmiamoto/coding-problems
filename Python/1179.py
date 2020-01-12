evens = []
odds = []

for i in range(15):
    n = int(input())

    if len(evens) == 5:
        [print('par[{}] = {}'.format(i, e)) for i, e in enumerate(evens)]
        evens = []

    if len(odds) == 5:
        [print('impar[{}] = {}'.format(i, e)) for i, e in enumerate(odds)]
        odds = []

    isEven = n % 2 == 0

    if isEven:
        evens.append(n)
    else:
        odds.append(n)

[print('impar[{}] = {}'.format(i, e)) for i, e in enumerate(odds)]
[print('par[{}] = {}'.format(i, e)) for i, e in enumerate(evens)]
