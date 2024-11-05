from math import sqrt, isqrt

def continued_fraction_gen(n):
    denominator, integer_part = 1, isqrt(n)
    current_term, final_term = 1, 2 * integer_part
    
    while current_term != final_term:
        current_term = int(denominator * (sqrt(n) + integer_part) / (n - integer_part ** 2))
        yield current_term
        denominator, integer_part = (n - integer_part ** 2) // denominator, \
                                    current_term * (n - integer_part ** 2) // denominator - integer_part

x_max, D_max = 0, None
for D in range(2, 1001):
    if sqrt(D).is_integer(): continue
    continued_fraction = [isqrt(D)] + list(continued_fraction_gen(D))

    if (len(continued_fraction) - 2) % 2 == 1: continued_fraction.pop()
    else: continued_fraction.extend(continued_fraction[1:-1])

    numerator, denominator = continued_fraction[-1], 1
    for term in reversed(continued_fraction[:-1]):
        numerator, denominator = term * numerator + denominator, numerator

    if numerator > x_max: x_max, D_max = numerator, D

print(D_max)