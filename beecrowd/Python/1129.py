letras = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E'}

while True:
    try:
        num_testes = int(input())
        for _ in range(num_testes):
            niveis = [int(x) for x in input().split()]
            resp = None
            for index, nivel in enumerate(niveis):
                if nivel <= 127:
                    if resp is None:
                        resp = index
                    else:
                        print('*')
                        break
            else:
                if resp is not None:
                    print(letras[str(resp)])
                else:
                    print('*')
    except:
        break
