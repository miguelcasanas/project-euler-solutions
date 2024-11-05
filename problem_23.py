LIMIT = 28_123

divsum = [0] * (LIMIT + 1)
for n in range(1, LIMIT // 2 + 1):
    for m in range(2 * n, LIMIT + 1, n):
        divsum[m] += n

is_abundant = lambda n: divsum[n] > n
abundants = list(filter(is_abundant, range(1, LIMIT + 1)))

is_sum = [False] * (LIMIT + 1)
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        ab = abundants[i] + abundants[j]
        if ab <= LIMIT: is_sum[ab] = True
        else: break

result = sum(i for i in range(LIMIT + 1) if not is_sum[i])
print(result)