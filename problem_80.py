from math import isqrt

def dsum(n): return sum(map(int, str(n)[:100]))

def sqrt_dsum(n):
    n *= 10**200

    x, f = 1, lambda x: (x + n // x) // 2
    while (new_x := f(x)) != x: x = new_x

    return dsum(x)

is_not_square = lambda n: isqrt(n)**2 != n
not_squares = filter(is_not_square, range(1, 101))
print(sum(map(sqrt_dsum, not_squares)))