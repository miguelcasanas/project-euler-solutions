from functools import cache

@cache
def chain_length(n):
    if n == 1: return 1
    next_term = 3*n + 1 if n % 2 else n >> 1
    return chain_length(next_term) + 1

print(max(range(1, 10**6), key=lambda n: chain_length(n)))