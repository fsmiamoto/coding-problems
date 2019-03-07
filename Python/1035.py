a, b, c, d = [int(a) for a in input().split()]

if a % 2 != 0 or b <= c or d <= a or c + d <= a + b or c <= 0 or d <= 0:
	print('Valores nao aceitos')
else:
	print('Valores aceitos') 