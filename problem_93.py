from itertools import product, combinations, permutations
from operator import add, sub, mul, truediv as div
from fractions import Fraction

sub2 = lambda x, y: sub(y, x)
div2 = lambda x, y: div(y, x)

all_ops = [add, sub, sub2, mul, div, div2]
operators = list(product(all_ops, repeat=3))
digs = list(combinations(map(Fraction, range(1, 10)), 4))

def integers(digits: tuple) -> set:
    ints = set()
    for ops, ds in product(operators, permutations(digits)):
        try:
            x = ops[0](ds[0], ds[1])
            for i in range(1, 3): x = ops[i](x, ds[i + 1])
            if x.denominator == 1 and x.numerator > 0:
                ints.add(x.numerator)
        except ZeroDivisionError: continue
    return ints

def consecutive(ints: set) -> int:
    for n in range(1, len(ints) + 1):
        if n not in ints: return n - 1
    return len(ints)

max_length, best_digits = 0, None
for digits in digs:
    consecutive_length = consecutive(integers(digits))
    if consecutive_length > max_length:
        max_length, best_digits = consecutive_length, digits

print(''.join(str(n) for n in best_digits))