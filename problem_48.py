MOD = 10**10

result = sum(pow(n, n, MOD) for n in range(1, 1001)) % MOD

print(result)