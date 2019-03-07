n = int(input())

testes = {'C': 0, 'R': 0, 'S':0}

for _ in range(n):
    qntd, tipo = input().split()
    testes[tipo] += int(qntd)

total = sum(testes.values())
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(testes['C']))
print('Total de ratos: {}'.format(testes['R']))
print('Total de sapos: {}'.format(testes['S']))
print('Percentual de coelhos: {:.2f} %'.format(100 * testes['C'] / total))
print('Percentual de ratos: {:.2f} %'.format(100 * testes['R'] / total))
print('Percentual de sapos: {:.2f} %'.format(100 * testes['S'] / total))
