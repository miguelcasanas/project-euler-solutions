from itertools import product

with open("0081_matrix.txt") as f:
    matrix = [
        [int(n) for n in row.split(",")]
        for row in f.read().strip().split("\n")
    ]

SIZE = len(matrix)

dp = [[0] * SIZE for _ in range(SIZE)]
dp[0][0] = matrix[0][0]

for k in range(1, SIZE):
    dp[0][k] = dp[0][k-1] + matrix[0][k]
    dp[k][0] = dp[k-1][0] + matrix[k][0]

for i, j in product(range(1, SIZE), repeat=2):
    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])