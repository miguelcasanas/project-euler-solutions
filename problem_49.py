from collections import defaultdict
from sympy import primerange
from itertools import combinations

primes = defaultdict(list)
for p in map(str, primerange(10**3, 10**4)):
    primes[tuple(sorted(p))].append(int(p))

for S in primes.values():
    if len(S) < 3: continue
    for comb in combinations(sorted(S), 3):
        a, b, c = comb
        if 2*b == a + c and a != 1487: 
            print(f"{a}{b}{c}")