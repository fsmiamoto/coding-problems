"""
1144 - Sequência lógica
"""
x = int(input())

for i in range(1, x+1):
    print('{} {} {}'.format(i, i**2, i**3))
    print('{} {} {}'.format(i, i**2+1, i**3+1))
