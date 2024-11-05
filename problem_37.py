from sympy import isprime

def left_truncatables():
    primes = ["3", "5", "7"]
    while primes:
        yield from map(int, primes)
        new_primes = []
        for prime in primes:
            for digit in map(str, range(1, 10)):
                new_prime = digit + prime
                if isprime(int(new_prime)):
                    new_primes.append(new_prime)
        primes = new_primes

def is_right_truncatable(n):
    if n < 10: return isprime(n)
    n //= 10
    return is_right_truncatable(n) if isprime(n) else False

primes = filter(is_right_truncatable, left_truncatables())
print(sum(primes, -15))