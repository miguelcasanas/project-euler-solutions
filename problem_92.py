from itertools import combinations_with_replacement as combs
from collections import Counter
from math import factorial as f, prod

def sqdsum(n):
    if n == 0: return 0
    q, r = divmod(n, 10)
    return r**2 + sqdsum(q)

def numbers(combo):
    combo = Counter(combo)
    combo['0'] = 7 - combo.total()
    return f(7) // prod(map(f, combo.values()))

def get_total(cnt, total=0):
    if len(cnt) <= 1: return total
    new_cnt = Counter()
    for k, v in cnt.items(): new_cnt[sqdsum(k)] += v
    total += new_cnt.pop(89)
    return get_total(new_cnt, total)

cnt = Counter()
for num_digits in range(1, 8):
    for combo in combs(map(str, range(1, 10)), num_digits):
        cnt[sqdsum(int(''.join(combo)))] += numbers(combo)

print(get_total(cnt))