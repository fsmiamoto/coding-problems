n = int(input())

carrinhos, bonecas = 0, 0

for _ in range(n):
    _, sexo = input().split(' ')
    if sexo == 'M':
        carrinhos += 1
    else:
        bonecas += 1

print('{} carrinhos'.format(carrinhos))
print('{} bonecas'.format(bonecas))
