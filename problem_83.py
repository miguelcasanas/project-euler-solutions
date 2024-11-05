from heapq import heappop, heappush

with open("0083_matrix.txt") as f:
    matrix = [
        [int(n) for n in row.split(",")]
        for row in f.read().strip().split("\n")
    ]

SIZE = len(matrix)
directions = (0, 1), (1, 0), (0, -1), (-1, 0)

dist = [[float('inf')] * SIZE for _ in range(SIZE)]
dist[0][0] = matrix[0][0]

queue = [(matrix[0][0], 0, 0)]

while queue:
    current_sum, x, y = heappop(queue)

    if (x, y) == (SIZE - 1, SIZE - 1): break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            new_sum = current_sum + matrix[nx][ny]

            if new_sum < dist[nx][ny]:
                dist[nx][ny] = new_sum
                heappush(queue, (new_sum, nx, ny))

print(current_sum)