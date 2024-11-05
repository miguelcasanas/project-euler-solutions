from fractions import Fraction as fr

product = 1
for n in range(10, 99):
    for d in range(n + 1, 100):
        n_1, n_0 = divmod(n, 10)
        d_1, d_0 = divmod(d, 10)
        f = fr(n, d)
        conds = [
             d_0 != 0 and n_0 == d_1 and f == fr(n_1, d_0),
             n_1 == d_0 and f == fr(n_0, d_1)
        ]
        if conds[0] or conds[1]: product *= f

print(product.denominator)