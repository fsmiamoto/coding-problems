notas = [float(x) for x in input().split()]
pesos = [2, 3, 4, 1]

media = 0
for n, p in zip(notas,pesos):
	media += n * p

media /= sum(pesos)

if media < 5.0:
	print('Media: {:.1f}'.format(media))
	print('Aluno reprovado.')
elif media >= 7.0:
	print('Media: {:.1f}'.format(media))
	print('Aluno aprovado.')
else:
	print('Media: {:.1f}'.format(media))
	print('Aluno em exame.')
	exame = float(input())
	print('Nota do exame: {:.1f}'.format(exame))
	media = 0.5 * (media + exame)
	if media < 5.0:
		print('Aluno reprovado.')
	else:
		print('Aluno aprovado.')
	print('Media final: {:.1f}'.format(media))
