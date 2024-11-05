# from math import comb
# print(comb(40, 20))

from functools import cache

@cache
def count_paths(i, j):
    if (i, j) == (0, 0): return 1
    paths = count_paths(i - 1, j) if i else 0
    paths += count_paths(i, j - 1) if j else 0
    return paths

print(count_paths(20, 20))