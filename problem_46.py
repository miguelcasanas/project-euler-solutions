from sympy import primerange, isprime
from math import isqrt
from itertools import product, count, filterfalse

LIMIT = 10**4

primes = list(primerange(LIMIT))
squares = [n**2 for n in range(1, isqrt(LIMIT))]

S = set()
for p, sq in product(primes, squares):
    S.add(p + 2*sq)

for n in filterfalse(isprime, count(9, 2)):
    if n not in S: break

print(n)