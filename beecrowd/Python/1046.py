inicio, fim = [int(x) for x in input().split()]

if fim > inicio:
	print('O JOGO DUROU {} HORA(S)'.format(fim - inicio))
else:
	print('O JOGO DUROU {} HORA(S)'.format(24 + fim - inicio))
