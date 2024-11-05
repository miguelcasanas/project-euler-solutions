from math import comb

def rectangles(width, height):
    return comb(width + 1, 2) * comb(height + 1, 2)

LIMIT = 10**3

min_diff = float('inf')
for w in range(1, LIMIT + 1):
    for h in range(w, LIMIT + 1):
        diff = abs(2_000_000 - rectangles(w, h))
        if diff < min_diff:
            min_diff, area = diff, w * h

print(area)