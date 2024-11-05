LIMIT = 10**6
phi = list(range(LIMIT + 1))

for p in range(2, LIMIT + 1):
    if phi[p] == p:
        for k in range(p, LIMIT + 1, p):
            phi[k] *= p - 1
            phi[k] //= p

maximum = 0
for n in range(2, LIMIT + 1):
    if (ratio := n / phi[n]) > maximum:
        maximum, n_max = ratio, n

print(n_max)