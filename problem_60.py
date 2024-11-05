from sympy import primerange, isprime
from itertools import combinations
from collections import defaultdict

primes = list(map(str, primerange(3, 10**4)))

def combines(p, q):
    return isprime(int(p + q)) and isprime(int(q + p))

friends = defaultdict(set)
for p, q in combinations(primes, 2):
    if combines(p, q):
        friends[p].add(q)
        friends[q].add(p)

def groups(group):
    if len(group) == 5:
        yield group
        return
    common = set.intersection(*(friends[p] for p in group))
    for new_p in common: yield from groups(group + (new_p,))

min_sum = float('inf')
for p in primes:
    for group in groups((p,)):
        if (s := sum(map(int, group))) > min_sum: continue
        min_sum = s

print(min_sum)