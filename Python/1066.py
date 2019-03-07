even = 0
odd = 0
pos = 0
neg = 0

for _ in range(5):
    value = int(input())
    if value % 2 == 0:
        even += 1
    else: 
        odd += 1
    if value > 0: 
        pos += 1
    elif value < 0:
        neg += 1
         
print('{} valor(es) par(es)'.format(even))
print('{} valor(es) impar(es)'.format(odd))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))
