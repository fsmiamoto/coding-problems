"""
1117 - Validação de Nota
"""

NUM_OF_NOTAS = 2

notas = []

while len(notas) < NUM_OF_NOTAS:
    nota = float(input())

    if nota < 0 or nota > 10:
        print('nota invalida')
    else:
        notas.append(nota)

print('media = {}'.format(sum(notas) / NUM_OF_NOTAS))
