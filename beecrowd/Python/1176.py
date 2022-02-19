def getNthFib(n: int, b: int) -> int:
    '''
    Calculates the Nth fibonacci number
    '''
    if n == 0:
        return 1
    if n == 1:
        return 1

    lastCalls = [0, 0]
    counter = 2
    while counter <= n:
        print(counter)
        nextCall = (lastCalls[0] + lastCalls[1] + 2) % b

        lastCalls[0] = lastCalls[1]
        lastCalls[1] = nextCall

        counter += 1

    return lastCalls[1] + 1


if __name__ == '__main__':
    cases = 1
    while True:
        n, b = [int(x) for x in input().split()]

        call = getNthFib(n, b)

        if n == 0 and b == 0:
            break

        print('Case {}: {} {} {}'.format(cases, n, b, call))
        cases += 1

