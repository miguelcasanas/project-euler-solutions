from more_itertools import flatten

def binomials(n):
    tri = [[1]]
    
    for i in range(1, n + 1):
        row = [1]
        for j in range(1, i):
            row.append(tri[i - 1][j - 1] + tri[i - 1][j])
        row.append(1)
        tri.append(row)
    
    yield from flatten(tri)

print(sum(1 for b in binomials(100) if b > 10**6))