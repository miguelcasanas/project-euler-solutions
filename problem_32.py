from string import digits
from itertools import combinations, permutations

def products():
    for p in permutations(digits[1:]):
        p = ''.join(p)
        for i, j in combinations(range(3, 6), 2):
            part = p[:i], p[i:j], p[j:]
            a, b, c = map(int, part)
            if a * b == c: yield c

print(sum(set(products())))