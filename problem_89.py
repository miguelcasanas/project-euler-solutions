R = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
    }
L = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2]

def to_decimal(r):
    dec = R[r[-1]]
    for i in range(len(r) - 1):
        a, b = r[i:i + 2]
        sgn = 1 if R[a] >= R[b] else -1
        dec += sgn * R[a]
    return dec

def roman_len(n):
    l = i = 0
    while n > 0:
        n, d = divmod(n, 10)
        l += L[d] if i < 3 else d
        i += 1
    return l

with open("0089_roman.txt") as f:
    romans = f.read().splitlines()

saved = lambda r: len(r) - roman_len(to_decimal(r))
print(sum(map(saved, romans)))