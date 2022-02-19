numOfProducts = int(input())

total = 0

for _ in range(numOfProducts):
    prod, qnt = [int(x) for x in input().split()]
    total += qnt * ((prod - 1000) + 0.5)

print('{:.2f}'.format(total))
