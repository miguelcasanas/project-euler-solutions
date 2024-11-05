f = lambda k, n: n * ((k - 2) * n - k + 4) // 2
S = {k: {f(k, n) for n in range(2, 10**5)} for k in [3,5,6]}

print(sorted(S[3] & S[5] & S[6])[1])