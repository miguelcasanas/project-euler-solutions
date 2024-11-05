from itertools import permutations

maximum = ""
for x in permutations(range(1, 11), 10):
    out, inn = x[:5], x[5:]
    if 10 in inn: continue

    target_sum = out[4] + inn[4] + inn[0]
    if not all(out[i] + inn[i] + inn[(i + 1) % 5] == target_sum for i in range(4)): continue

    i0 = min(range(5), key=lambda i: out[i])
    string = "".join(
        f"{out[(i0+i)%5]}{inn[(i0+i)%5]}{inn[(i0+i+1)%5]}"
        for i in range(5)
    )

    if string > maximum: maximum = string

print(maximum)