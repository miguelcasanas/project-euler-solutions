LIMIT = 12000

N = [2 * LIMIT] * (LIMIT + 1)

def productsum(prod, suma, n, i0):
    if (k := n + prod - suma) > LIMIT: return
    if prod < N[k]: N[k] = prod
    for i in range(i0, 2 * LIMIT // prod + 1):
        productsum(prod * i, suma + i, n + 1, i)

productsum(1, 0, 0, 2)
print(sum(set(N[2:])))