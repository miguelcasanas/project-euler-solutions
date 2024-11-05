from itertools import count, takewhile
from more_itertools import ilen

def p_gen():
    p_values = [1]
    yield 1
    for n in count(1):
        total = 0
        for k in count(1):
            g_k = k * (3 * k - 1) // 2
            g_neg_k = k * (3 * k + 1) // 2
            
            if g_k > n: break
            
            sign = (2 * (k % 2) - 1)
            total += sign * p_values[n - g_k]
            if g_neg_k <= n:
                total += sign * p_values[n - g_neg_k]

        p_values.append(total)
        yield total

print(ilen(takewhile(lambda x: x % 10**6, p_gen())))