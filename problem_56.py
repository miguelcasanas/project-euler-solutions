from itertools import product

def digit_sum(n): return sum(map(int, str(n)))

max_dsum = 0
for a, b in product(range(100), repeat=2):
    max_dsum = max(max_dsum, digit_sum(a**b))

print(max_dsum)