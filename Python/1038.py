produtos = {'1': 4, '2': 4.50, '3': 5, '4': 2.00, '5': 1.50}

cod, qntd = input().split()
print('Total: R$ {:.2f}'.format(int(qntd) * produtos[cod]))
