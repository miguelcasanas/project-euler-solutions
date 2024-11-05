from string import digits
from itertools import permutations
from sympy import isprime

def find_pandigital_prime(n):
    odd_pandigitals = []
    for perm in permutations(digits[1:n + 1]):
        if perm[-1] in "2468": continue
        odd_pandigitals.append(int(''.join(perm)))
    
    odd_pandigitals.sort(reverse=True)

    for p in odd_pandigitals:
        if isprime(p): return p

for n in range(9, 3, -1):
    if (p := find_pandigital_prime(n)): break

print(p)