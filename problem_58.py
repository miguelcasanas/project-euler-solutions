from itertools import count, batched
from sympy import isprime

def corner_gen():
    for n in count(3, 2):
        sq = n**2
        step = (sq - (n - 2)**2) // 4
        for _ in range(3):
            sq -= step
            yield sq

prime_count = 0
for i, corners in enumerate(batched(corner_gen(), 3), 1):
    prime_count += sum(map(isprime, corners))
    if prime_count / (4*i + 1) < 0.1: break

print(2*i + 1)