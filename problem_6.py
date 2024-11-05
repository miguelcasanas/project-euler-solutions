T = lambda n: n * (n + 1) // 2
P = lambda n: T(n) * (2 * n + 1) // 3

print(T(100)**2 - P(100))