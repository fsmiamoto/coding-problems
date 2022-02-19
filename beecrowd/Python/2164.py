
n = int(input())


def fib(n):
    a = (0.5 + 0.5 * 5 ** 0.5) ** n - (0.5 - 0.5 * 5 ** 0.5) ** n
    return a / 5 ** 0.5


print('{:.1f}'.format(fib(n)))
