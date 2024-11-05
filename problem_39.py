from itertools import count
from math import gcd
from collections import Counter

LIMIT = 1000

def triples():
    for m in count(2):
        for n in range(1, m):
            if (m + n) % 2 != 1: continue
            if gcd(m, n) != 1: continue
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if a + b + c > LIMIT: return
            yield a, b, c

perims = Counter()
for a, b, c in triples():
    for k in count(1):
        ka, kb, kc = k*a, k*b, k*c
        if (p := ka + kb + kc) > LIMIT: break
        perims[p] += 1

print(max(perims, key=lambda p: perims[p]))