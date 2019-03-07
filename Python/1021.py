notas = (100, 50, 20, 10, 5, 2)
moedas = (100, 50, 25, 10, 5, 1)

total = 576.73

total_notas = int(total)
total_moedas = round(100 * (total - total_notas))

print('NOTAS:')
for valor in notas:
    num_notas = total_notas // valor
    total_notas = total_notas % valor
    print('{} nota(s) de R$ {:.2f}'.format(num_notas, valor))

if total_notas != 0:
    total_moedas += 100 * total_notas

print('MOEDAS:')
for valor in moedas:
    num_moedas = total_moedas // valor
    total_moedas = total_moedas % valor
    print('{} moeda(s) de R$ {:.2f}'.format(num_moedas, valor / 100))
