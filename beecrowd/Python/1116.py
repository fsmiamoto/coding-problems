num_of_cases = int(input())

for _ in range(num_of_cases):
    a, b = [int(x) for x in input().split()]

    if b == 0:
        print('divisao imposssivel')
    else:
        print('{:.1f}'.format(a / b))
    