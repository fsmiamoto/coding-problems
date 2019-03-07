from math import sqrt as raiz

a, b, c = [float(x) for x in input().split()]

delta = b**2 - 4*a*c

if delta < 0 or a == 0:
	print('Impossivel calcular')
else:
	r1 = (- b + raiz(delta)) / (2*a)
	r2 = (- b - raiz(delta)) / (2*a)	
	print('R1 = {:.5f}'.format(r1))
	print('R2 = {:.5f}'.format(r2))