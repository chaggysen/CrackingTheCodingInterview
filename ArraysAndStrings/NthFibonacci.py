def getNthFib(n):
    memo = {}
    memo[1] = 0
    memo[2] = 1
    return getNthFibHelper(memo, n)


def getNthFibHelper(memo, n):
    if n in memo:
        return memo[n]
    else:
        value = getNthFibHelper(memo, n - 1) + getNthFibHelper(memo, n - 2)
        memo[n] = value
        return value
