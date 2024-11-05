from sympy import primerange

LIMIT = 10**6
primes = list(primerange(LIMIT))

cumsum = [0]
for p in primes: cumsum.append(cumsum[-1] + p)

def find_prime():
    for i in range(l := len(primes), 1, -1):
        for j in range(l - i + 1):
            if (s := cumsum[j+i] - cumsum[j]) > LIMIT: break
            if s in primes: return s

print(find_prime())