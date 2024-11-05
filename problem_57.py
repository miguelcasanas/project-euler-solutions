from fractions import Fraction

convergents, count = [1], 0
for _ in range(1000):
    new_conv = 1 + Fraction(1, 1 + convergents[-1])
    n, d = new_conv.numerator, new_conv.denominator
    if len(str(n)) > len(str(d)): count += 1
    convergents.append(new_conv)

print(count)