"""
1131 - Grenais
"""


def resultado_grenal():
    golsInter, golsGremio = [int(gols) for gols in input().split()]

    if golsInter > golsGremio:
        return 'Inter'
    elif golsInter < golsGremio:
        return 'Gremio'
    else:
        return 'Empates'


num_of_grenais = 0
resultados = {
    'Inter': 0,
    'Gremio': 0,
    'Empates': 0
}

while True:
    novo_resultado = resultado_grenal()

    resultados[novo_resultado] += 1
    num_of_grenais += 1

    print('Novo grenal (1-sim 2-nao)')
    resposta = int(input())

    if resposta == 1:
        continue
    elif resposta == 2:
        break

# Apresenta resultados
print('{} grenais'.format(num_of_grenais))

for clube, num_of_vitorias in resultados.items():
    print('{}:{}'.format(clube, num_of_vitorias))

if resultados['Inter'] > resultados['Gremio']:
    print('Inter venceu mais')
elif resultados['Inter'] < resultados['Gremio']:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
