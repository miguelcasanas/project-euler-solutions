from itertools import count, takewhile, product
from more_itertools import ilen
from sympy import isprime

def formula(a, b):
    for n in count():
        yield n**2 + a*n + b

def count_primes(a, b):
    return ilen(takewhile(isprime, formula(a, b)))

max_primes = prod = 0
for a, b in product(range(-999, 1000, 2), repeat=2):
    if (primes := count_primes(a, b)) > max_primes:
        max_primes, prod = primes, a * b

print(prod)