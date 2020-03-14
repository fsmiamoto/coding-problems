numOfCases = int(input())

for _ in range(numOfCases):
    n = int(input())
    since = 2015 - n
    if since > 0:
        print('{} D.C.'.format(since))
    else:
        print('{} A.C.'.format(-since+1))
