x, y = [float(a) for a in input().split()]

if x * y < 0:
	if x < 0:
		print('Q2')
	else: 
		print('Q4')
elif x * y > 0:
	if x < 0:
		print('Q3')
	else:
		print('Q1')
else:
	if x != 0:
		print('Eixo X')
	elif y != 0:
		print('Eixo Y')
	else:
		print('Origem') 
