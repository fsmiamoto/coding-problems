num_pessoas, salto = [int(x) for x in input().split()]

lista = list(range(1, num_pessoas + 1))

while len(lista) > 1:
	print(lista)
	lista = lista[::salto]
	
print('Case {}: {}'.format(1, lista))
