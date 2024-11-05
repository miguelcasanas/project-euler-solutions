from itertools import product, combinations as combs
from math import dist as d

grid = set()
for p in product(range(51), repeat=2):
    if p != (0, 0): grid.add(p)

p0, count = (0, 0), 0
for p1, p2 in combs(grid, 2):
    if p1[0]*p2[1] == p2[0]*p1[1]: continue
    a, b, c = d(p0, p1), d(p1, p2), d(p2, p0)
    a, b, c = sorted([a, b, c])
    if abs(a**2 + b**2 - c**2) < 0.1: count += 1

print(count)