from sympy import primerange
from itertools import takewhile

LIMIT = 50_000_000

primes = list(primerange(int(LIMIT**0.5)))

pow_gen = lambda exp: (p**exp for p in primes)
powers = {
    k: list(takewhile(lambda x: x < LIMIT, pow_gen(k)))
    for k in [2, 3, 4]
}

numbers = set()
for a in powers[2]:
    for b in powers[3]:
        if (n := a + b) >= LIMIT: break
        for c in powers[4]:
            if (m := n + c) >= LIMIT: break
            numbers.add(m)

print(len(numbers))