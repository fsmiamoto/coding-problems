def josephus(numPessoas, passo):
    pessoas = list(range(1, numPessoas + 1))
    pessoaAtual = 0
    qntdPessoas = len(pessoas)
    while qntdPessoas > 1:
        pessoaAtual = removePessoa(pessoas, pessoaAtual, passo, qntdPessoas)
        qntdPessoas = len(pessoas)

    return pessoas[0]


def removePessoa(pessoas, inicio, passo, qntdPessoas):
    morre = inicio + passo - 1

    while morre >= qntdPessoas:
        morre -= qntdPessoas

    del pessoas[morre]

    return morre


if __name__ == '__main__':
    numDeTestes = int(input())
    for i in range(numDeTestes):
        numPessoas, salto = [int(x) for x in input().split()]
        print('Case {}: {}'.format(i + 1, josephus(numPessoas, salto)))
