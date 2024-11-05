from itertools import combinations

LIMIT = 2400

P = {n * (3*n - 1) // 2 for n in range(1, LIMIT + 1)}

for a, b in combinations(P, 2):
    if a + b in P and (D := abs(a - b)) in P: print(D)