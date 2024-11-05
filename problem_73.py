from math import gcd

LIMIT = 12000

count = 0
for d in range(2, LIMIT + 1):
    n_min, n_max = d // 3 + 1, (d - 1) // 2
    for n in range(n_min, n_max + 1):
        if gcd(n, d) == 1: count += 1

print(count)