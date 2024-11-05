with open("0082_matrix.txt") as f:
    matrix = [
        [int(n) for n in row.split(",")]
        for row in f.read().strip().split("\n")
    ]

SIZE = len(matrix)

dp = [[float('inf')] * SIZE for _ in range(SIZE)]
for i in range(SIZE): dp[i][0] = matrix[i][0]

for j in range(1, SIZE):
    for i in range(SIZE):
        dp[i][j] = dp[i][j-1] + matrix[i][j]

    for i in range(1, SIZE):
        dp[i][j] = min(dp[i][j], dp[i-1][j] + matrix[i][j])

    for i in range(SIZE - 2, -1, -1):
        dp[i][j] = min(dp[i][j], dp[i+1][j] + matrix[i][j])

result = min(dp[i][-1] for i in range(SIZE))
print(result)