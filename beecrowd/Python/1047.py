h1, m1, h2, m2 = [int(x) for x in input().split()]

if h2 > h1:
    if m2 >= m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h2 - h1, m2 - m1))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h2 - h1 - 1, 60 - (m1 - m2)))
elif h2 < h1:
    if m2 >= m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24 + h2 - h1, m2 - m1))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24 + h2 - h1 - 1, 60 - (m1 - m2)))
else:
    if m2 > m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(0, m2 - m1))
    elif m2 < m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24 + h2 - h1 - 1, 60 - (m1 - m2)))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24, 0))