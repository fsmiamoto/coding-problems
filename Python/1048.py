salario = float(input())

# Limites inferiores e suas respectiva taxas
percentuais = [(400, 15), (800, 12), (1200, 10), (2000, 7)]

for lim, taxa in percentuais:
    if salario <= lim:
        reajuste = 0.01 * taxa * salario
        print('Novo salario: {0:.2f}\nReajuste ganho: {1:.2f}\nEm percentual: {2} %'.format(salario + reajuste, reajuste, taxa))
        break
else:
    reajuste = 0.01 * 4 * salario
    print('Novo salario: {0:.2f}\nReajuste ganho: {1:.2f}\nEm percentual: {2} %'.format(salario + reajuste, reajuste, 4))

