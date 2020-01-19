while True:
    n = int(input())

    if n == 0:
        break

    for i in range(1,n+1):
        for j in range(1,n+1):
            valor = 1
            maior, menor = (i,j) if i > j else (j,i)
            valor += min((menor-1, n-maior))

            if j == n:
                print('{:3d}'.format(valor))
                continue

            print('{:3d}'.format(valor), end=' ')

    print()
