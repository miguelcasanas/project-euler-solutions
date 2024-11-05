def is_palindromic(n):
    n = str(n)
    return n == n[::-1]

largest = 0
for x in range(100, 1000):
    for y in range(x, 1000):
        if is_palindromic(product := x * y):
            largest = max(largest, product)

print(largest)