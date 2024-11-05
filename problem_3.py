N = 600_851_475_143

for k in range(2, N + 1):
    while N % k == 0: N //= k
    if N == 1: break

print(k)