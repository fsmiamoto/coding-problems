jump, numOfPipes = [int(x) for x in input().split()]

pipes = [int(x) for x in input().split()]

lost = False
for current,next in zip(pipes,pipes[1:]):
    if abs(next-current) > jump:
        lost = True
        break

if lost:
    print('GAME OVER')
else:
    print('YOU WIN')
