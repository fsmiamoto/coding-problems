numOfCases = int(input())

for _ in range(numOfCases):
    playerA, oddEvenA,playerB,oddEvenB = input().split()
    playerANum,playerBNum = [int(x) for x in input().split()]
    total = playerBNum + playerANum
    if total % 2 == 0:
        if oddEvenA == "PAR":
            print(playerA)
        else:
            print(playerB)
    else:
        if oddEvenA == "IMPAR":
            print(playerA)
        else:
            print(playerB)


