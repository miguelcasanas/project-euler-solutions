from itertools import count
from math import gcd
from collections import Counter

LIMIT = 1_500_000

def triples():
    for m in count(2):
        if 2 * m * (m + 1) > LIMIT: break
        for n in range(1, m):
            if (m + n) % 2 != 1: continue
            if gcd(m, n) != 1: continue
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if (perimeter := a + b + c) > LIMIT: break
            yield a, b, c

perims = Counter()
for a, b, c in triples():
    for k in count(1):
        ka, kb, kc = k * a, k * b, k * c
        if (p := ka + kb + kc) > LIMIT: break
        perims[p] += 1

print(sum(1 for p in perims if perims[p] == 1))