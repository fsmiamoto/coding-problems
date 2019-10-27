def getNthFib(n: int) -> int:
    '''
    Calculates the Nth fibonacci number
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1

    lastTwo = [0, 1]
    counter = 2
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1

    return lastTwo[1]


if __name__ == '__main__':
    numOfCases = int(input())
    for _ in range(numOfCases):
        x = int(input())
        print('Fib({}) = {}'.format(x, getNthFib(x)))
