LIMIT = 10**7
phi = list(range(LIMIT + 1))
ratio = {}

for p in range(2, LIMIT + 1):
    if phi[p] == p:
        for k in range(p, LIMIT + 1, p):
            phi[k] *= p - 1
            phi[k] //= p
    ratio[p] = p / phi[p]

def is_permutation(n):
    return sorted(str(n)) == sorted(str(phi[n]))

minimum = float('inf')
for n in range(2, LIMIT + 1):
    if ratio[n] < minimum and is_permutation(n):
        minimum, n_min = ratio[n], n

print(n_min)