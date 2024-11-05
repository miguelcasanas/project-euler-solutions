from sympy import primerange, isprime
from itertools import combinations
from functools import cache

primes = map(str, primerange(10**5, 10**6))

def pattern_gen(p):
    p, l = list(p), len(p)
    for indexes in combinations(range(l), 3):
        pattern = p.copy()
        for i in indexes: pattern[i] = '*'
        yield ''.join(pattern)

def matching(pattern):
    digits = set("0123456789")
    if pattern[-1] == '*': digits -= set("02468")
    if pattern[0] == '*': digits -= {'0'}

    for d in digits: yield pattern.replace('*', d)

def find_prime():
    @cache
    def is_prime(n): return isprime(int(n))

    for p in primes:
        for pattern in pattern_gen(p):
            not_prime_count, p_list = 0, []
            for p in matching(pattern):
                if is_prime(p): p_list.append(p)
                else:
                    not_prime_count += 1
                    if not_prime_count > 2: break
            else:
                if len(p_list) == 8: return min(p_list)

print(find_prime())