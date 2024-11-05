from math import factorial
from functools import cache
from itertools import combinations_with_replacement
from string import digits

f = {str(n): factorial(n) for n in range(10)}

@cache
def dfsum(n):
    return tuple(sorted(str(sum(f[d] for d in n))))

def chain_len(n, chain=[]):
    if not chain: chain = [n]
    if len(chain) > 60: return None
    if (dfs := dfsum(n)) in chain: return len(chain)
    return chain_len(dfs, chain + [dfs])

target = set()
for l in range(1, 7):
    for comb in combinations_with_replacement(digits, l):
        s = tuple(sorted(comb))
        if chain_len(comb) == 60: target.add(s)

count = 0
for n in map(str, range(1, 10**6)):
    if tuple(sorted(n)) in target:
        count += 1

print(count)