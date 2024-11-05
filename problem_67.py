with open("0067_triangle.txt") as f:
    triangle = f.read()

T = [
    [int(n) for n in row.split()]
    for row in triangle.splitlines()
]

for i in range(len(T) - 2, -1, -1):
    for j in range(i + 1):
        T[i][j] += max(T[i + 1][j], T[i + 1][j + 1])

print(T[0][0])