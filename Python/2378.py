from sys import stdin

atual = 0
excedeu = False

cap_max = stdin.line().split()[1]

for line in stdin:
	saiu, entrou = [int(x) for x in line.split()]
	atual = atual + entrou - saiu
	if atual > cap_max:
		excedeu = True
if excedeu:
	print('S')
else:
	print('N')