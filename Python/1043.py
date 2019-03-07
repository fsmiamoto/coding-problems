lados = [float(x) for x in input().split()]
lados.sort(reverse=True)
a, b, c = lados

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    else:
        if a**2 > b**2 + c**2:
            print('TRIANGULO OBTUSANGULO')
        else:
            print('TRIANGULO ACUTANGULO')
        if a == b and b == c:
            print('TRIANGULO EQUILATERO')
        elif a == b or b == c:
            print('TRIANGULO ISOSCELES')
        
