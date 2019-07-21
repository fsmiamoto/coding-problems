while True:
    # Read values
    a, b = (int(x) for x in input().split())

    # End signal
    if a == 0 or b == 0:
        break
    
    if a > 0:
        if b > 0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if b > 0:
            print('segundo')
        else:
            print('terceiro')