from sympy import primerange
from more_itertools import first_true

primes = list(primerange(1000))

def pparts(n, i=len(primes) - 1):
    if n == 0: return 1
    if n < 0 or i < 0: return 0

    with_prime = pparts(n - primes[i], i)
    without_prime = pparts(n, i - 1)
    return with_prime + without_prime

print(first_true(primes, pred=lambda p: pparts(p) > 5000))