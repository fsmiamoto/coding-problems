n = int(input())

cups = {'A':0,'B':0,'C':0}

initialPosition = input()

cups[initialPosition] = 1

for _ in range(n):
    movement = int(input())
    if movement == 1:
        cups['A'], cups['B'] = cups['B'], cups['A']
    elif movement == 2:
        cups['B'], cups['C'] = cups['C'], cups['B']
    else:
        cups['A'], cups['C'] = cups['C'], cups['A']

for k in cups:
    if cups[k] == 1:
        print(k)
