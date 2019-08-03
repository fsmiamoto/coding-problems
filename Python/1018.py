notas = (100, 50, 20, 10, 5, 2, 1)
total = int(input())

print(total)

for value in notas:
    num_notas = total // value  # Divisão inteira
    total -= value * num_notas
    print('{} nota(s) de R$ {},00'.format(num_notas, value))
