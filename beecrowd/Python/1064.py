qntd_pos = 0
soma = 0

for _ in range(6):
    num = input()
    if float(num) > 0:
        qntd_pos += 1
        soma += float(num)

print('{} valores positivos'.format(qntd_pos))
print('{:.2f}'.format(soma/6))
