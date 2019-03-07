a = int(input())
b = int(input())

if a > b:
    a, b = b, a
    
if a % 2 == 0:
    print(sum([x for x in range(a + 1, b, 2)]))
else:
    print(sum([x for x in range(a + 2, b, 2)]))
