LIMIT = 25_320

d = [0] * (LIMIT + 1)
for n in range(1, LIMIT + 1):
    for m in range(2*n, LIMIT + 1, n): d[m] += n

def is_amicable(n):
    if (dn := d[n]) == n: return False
    return d[dn] == n

print(sum(filter(is_amicable, range(10_000))))