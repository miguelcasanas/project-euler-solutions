# from itertools import count
# from more_itertools import first
# from sympy import divisor_count
# T = (n * (n + 1) // 2 for n in count(1))
# print(first(filter(lambda x: divisor_count(x) > 500, T)))

from collections import Counter
from math import prod
from itertools import count

LIMIT = 10**5

smallest = list(range(LIMIT + 1))
for p in range(2, LIMIT + 1):
    if smallest[p] == p:
        for i in range(p**2, LIMIT + 1, p):
            smallest[i] = p

def factorint(n):
    factors = Counter()
    while n > 1:
        if n > LIMIT:
            for p in range(2, LIMIT + 1):
                if smallest[p] != p: continue
                if n % p == 0: break
        else: p = smallest[n]
        factors[p] += 1
        n //= p
    return factors

def divisor_count(n):
    return prod(m + 1 for m in factorint(n).values())

triangle_numbers = (n * (n + 1) // 2 for n in count(1))

for t in triangle_numbers:
    if divisor_count(t) > 500: break

print(t)