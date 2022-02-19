while True:
	try:
		num_botas = int(input())
		botas = dict()

		for _ in range(num_botas):
			tam, lado = [a for a in input().split()]
			if tam not in botas:
				botas[tam] = [0, 0]
			if lado == 'E':
				botas[tam][0] += 1	
			else:
				botas[tam][1] += 1

		total_pares = 0
		for qntd in botas.values():
			total_pares += min(qntd)
		print(total_pares)
	except:
		break
