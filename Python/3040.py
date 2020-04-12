numOfCases = int(input())

for _ in range(numOfCases):
    height, diameter, numOfTwigs = [int(x) for x in input().split(' ')]

    if height >= 200 and height <= 300 and diameter >= 50 and numOfTwigs >= 150:
        print('Sim')
    else:
        print('Nao')
