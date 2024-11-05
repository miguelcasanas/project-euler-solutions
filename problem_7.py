# from sympy import prime
# print(prime(10_001))

LIMIT = 10**6

is_prime = [True] * (LIMIT + 1)
for p in range(2, LIMIT + 1):
    if is_prime[p]:
        for i in range(p**2, LIMIT + 1, p):
            is_prime[i] = False

primes = [p for p in range(2, LIMIT + 1) if is_prime[p]]

print(primes[10_000])