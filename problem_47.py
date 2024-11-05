from sympy import primerange
from more_itertools import windowed

LIMIT = 2*10**5

primes = primerange(LIMIT)
factors = [0] * (LIMIT + 1)

for p in primes:
    for m in range(p, LIMIT + 1, p):
        factors[m] += 1

for n, w in enumerate(windowed(factors, 4)):
    if set(w) == {4}: break

print(n)