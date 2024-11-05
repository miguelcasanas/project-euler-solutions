def find_triplet():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if c <= b: break
            if a**2 + b**2 == c**2:
                return a, b, c

a, b, c = find_triplet()
print(a * b * c)