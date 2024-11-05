from functools import cache

@cache
def p(n, k):
    if n == 0 and k == 0: return 1

    if not (n == 0 and k == 0):
        if n <= 0 or k <= 0:
            return 0

    return p(n - k, k) + p(n - 1, k - 1)

n = 100
print(sum(p(n, k) for k in range(2, n + 1)))