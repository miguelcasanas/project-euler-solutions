f = [1]
for n in range(1, 10): f.append(n * f[-1])

def dfsum(n):
    return sum(f[d] for d in map(int, str(n)))

is_factorion = lambda n: dfsum(n) == n
print(sum(filter(is_factorion, range(3, 7 * f[9]))))