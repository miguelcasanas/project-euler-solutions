import re
from itertools import product

with open("p096_sudoku.txt") as f:
    rows = re.findall(r'\d{9}', f.read())

sudokus = [
    [list(map(int, rows[9*i + j])) for j in range(9)]
    for i in range(len(rows) // 9)
]

def is_valid(sudoku, i, j, n):
    for k in range(9):
        if sudoku[i][k] == n or sudoku[k][j] == n:
            return False

    s_i, s_j = 3 * (i // 3), 3 * (j // 3)
    ranges = range(s_i, s_i + 3), range(s_j, s_j + 3)
    for i, j in product(*ranges):
        if sudoku[i][j] == n: return False
    return True

def solve(sudoku):
    for i, j in product(range(9), repeat=2):
        if sudoku[i][j] != 0: continue
        for n in range(1, 10):
            if is_valid(sudoku, i, j, n):
                sudoku[i][j] = n
                if solve(sudoku): return True
                sudoku[i][j] = 0
        return False
    return True

result = 0
for s in sudokus:
    solve(s)
    result += sum(s[0][j] * 10**(2 - j) for j in range(3))

print(result)