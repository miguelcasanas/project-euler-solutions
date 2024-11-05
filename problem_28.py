T = lambda n: n * (n + 1) // 2
P = lambda n: T(n) * (2 * n + 1) // 3

print(16 * P(500) + 4 * T(500) + 4 * 500 + 1)