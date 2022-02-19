while True:
    # Read values
    A, B = (int(x) for x in input().split())

    # End signal
    if A == 0 or B == 0:
        break

    if A > 0:
        if B > 0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if B > 0:
            print('segundo')
        else:
            print('terceiro')
