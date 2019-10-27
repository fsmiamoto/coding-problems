for i in range(11):
    I = 0.2*i
    for j in range(3):
        J = j + 1 + I
        if I.is_integer():
            print('I={}'.format(int(I)), end='')
        else:
            print('I={:.1f}'.format(I), end='')
        if J.is_integer():
            print(' J={}'.format(int(J)))
        else:
            print(' J={:.1f}'.format(J))
