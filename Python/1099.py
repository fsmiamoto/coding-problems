casos_teste = int(input())

for _ in range(casos_teste):
    a, b = (int(x) for x in input().split())
    # a sempre menor que b
    a, b = (a, b) if b > a else (b, a)
    soma = sum([x for x in range(a + 1, b) if x % 2 == 1])
    print(soma)
