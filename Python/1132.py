"""
1132 - Múltiplos de 13
"""

a = int(input())
b = int(input())

a, b = (a, b) if b > a else (b, a)

resultado = sum((num for num in range(a, b+1) if num % 13 != 0))
print(resultado)
