from math import gcd

LIMIT = 10**6

k = LIMIT // 7
n, d = 3*k - 1, 7*k

if gcd(n, d) == 1: print(n)