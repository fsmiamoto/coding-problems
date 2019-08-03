"""
1118 - Várias notas com validação
"""

NUM_OF_NOTAS = 2


def calcula_media():
    notas = []

    while len(notas) < NUM_OF_NOTAS:
        nota = float(input())

        if nota < 0 or nota > 10:
            print('nota invalida')
        else:
            notas.append(nota)

    print('media = {:.2f}'.format(sum(notas) / NUM_OF_NOTAS))


calcula_media()

while True:
    print('novo calculo (1-sim 2-nao)')
    resposta = int(input())

    if resposta == 1:
        calcula_media()
    elif resposta == 2:
        break
    else:
        continue
