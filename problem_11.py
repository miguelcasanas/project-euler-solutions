from itertools import product
from math import prod

numbers = """GRID HERE"""

grid = [
    list(map(int, row.split()))
    for row in numbers.splitlines()
]

SIZE = len(grid)

def groups():
    for i, j in product(range(SIZE), range(SIZE - 3)):
        yield grid[i][j:j + 4]
        yield [grid[j + k][i] for k in range(4)]
        if i < SIZE - 3:
            yield [grid[i + k][j + k] for k in range(4)]
            yield [grid[i + 3 - k][j + k] for k in range(4)]
            
print(max(map(prod, groups())))