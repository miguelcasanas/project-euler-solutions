from fractions import Fraction as f

def coeff(k):
    if k == 0: return 2
    return 2 * (k + 1) // 3 if (k + 1) % 3 == 0 else 1

def conv(n):
    if n == 0: return f(coeff(0))
    else: return f(coeff(n)) + f(1, conv(n - 1))

print(sum(map(int, str(conv(99).numerator))))