# from math import lcm
# print(lcm(*range(1, 21)))

from collections import Counter
from math import prod

def factorint(n):
    factors = Counter()
    for k in range(2, n + 1):
        while n % k == 0:
            factors[k] += 1
            n //= k
        if n == 1: return factors

lcm_factors = Counter()
for n in range(2, 21):
    for p, m in factorint(n).items():
        lcm_factors[p] = max(lcm_factors[p], m)

print(prod(p**m for p, m in lcm_factors.items()))