n = int(input())

count = {
    'hobbits': 0,
    'humans': 0,
    'elves': 0,
    'dwarfs': 0,
    'mages': 0,
}

for _ in range(n):
    _, race = input().split(' ')

    if race == 'A':
        count['dwarfs'] += 1
    elif race == 'E':
        count['elves'] += 1
    elif race == 'M':
        count['mages'] += 1
    elif race == 'X':
        count['hobbits'] += 1
    elif race == 'H':
        count['humans'] += 1

print('{} Hobbit(s)'.format(count['hobbits']))
print('{} Humano(s)'.format(count['humans']))
print('{} Elfo(s)'.format(count['elves']))
print('{} Anao(s)'.format(count['dwarfs']))
print('{} Mago(s)'.format(count['mages']))
