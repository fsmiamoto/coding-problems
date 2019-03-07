while True:
    try:
        entrada = input()
        num_1 = entrada.count('1')
        if num_1 % 2 == 0:
            print(entrada + '0')
        else:
            print(entrada + '1')
    except:
        break
