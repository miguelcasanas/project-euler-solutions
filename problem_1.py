LIMIT = 1000

# condition = lambda x: x % 3 == 0 or x % 5 == 0
# print(sum(filter(condition, range(LIMIT))))

def S(k):
    T = lambda n: n * (n + 1) // 2
    return k * T((LIMIT - 1) // k)

print(S(3) + S(5) - S(15))