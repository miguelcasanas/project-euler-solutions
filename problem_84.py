import numpy as np
from collections import defaultdict
from itertools import product

results = defaultdict(float)
P = np.zeros((40, 40))
prob_vec = np.zeros(40); prob_vec[0] = 1.0

for i, j in product(range(1, 5), repeat=2):
    results[i + j] += 1 / 16

for i in range(40):
    for value, p in results.items():
        nxt = (i + value) % 40
        if nxt == 30: P[i][10] += p
        elif nxt in {2, 17, 33}:
            P[i][0] += p / 16
            P[i][10] += p / 16
            P[i][nxt] += 14 * p / 16
        elif nxt in {7, 22, 36}:
            for j in [0, 5, 10, 11, 12, 15, 24, 39]:
                P[i][j] += p / 16
            P[i][(nxt - 3) % 40] += p / 16
            P[i][nxt] += 6 * p / 16
        else: P[i][nxt] += p

for _ in range(200): prob_vec = prob_vec @ P

most_popular = np.argsort(prob_vec)[-3:][::-1]
print(''.join(f"{square:02}" for square in most_popular))