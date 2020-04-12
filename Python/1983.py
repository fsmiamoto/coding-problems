n = int(input())

choosen = [0,0]

for _ in range(n):
    code, grade = [float(x) for x in input().split()]
    if grade > choosen[1]:
        choosen = [code,grade]

if choosen[1] < 8:
    print('Minimum note not reached')
else:
    print(int(choosen[0]))
