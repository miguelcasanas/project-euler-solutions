from math import sqrt
from itertools import count

def period(n):
    p, q, states = int(root := sqrt(n)), 1, {}
    if root.is_integer(): return 0
    for i in count(1):
        q = (n - p**2) / q
        floor = int((root + p) / q)
        p = -1 * (p - (floor * q))
        if (p, q) in states: return i - states[p, q]
        states[p, q] = i

print(sum(1 for n in range(10**4) if period(n) % 2))