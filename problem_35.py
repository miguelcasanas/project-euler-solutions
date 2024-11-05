from sympy import primerange

def rotations(n):
    for i in range(len(n)):
        yield n[i:] + n[:i]

primes = set(map(str, primerange(10**6)))

circular_primes = set()
for p in primes:
    if p in circular_primes: continue
    if set(p) & set("02468"): continue
    rots = []
    for r in rotations(p):
        if r not in primes: break
        rots.append(r)
    else: circular_primes.update(rots)

print(len(circular_primes) + 1)