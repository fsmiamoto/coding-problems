
"""
1133 - Resto da divisão
"""

a = int(input())
b = int(input())

a, b = (a, b) if b > a else (b, a)

[print(num) for num in range(a+1, b) if num % 5 == 2 or num % 5 == 3]
